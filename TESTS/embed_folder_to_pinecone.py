# embed_folder_to_pinecone.py
import os, json, time
from pathlib import Path

# ---- CONFIG UTILISATEUR ----
ROOT_DIR = "/Users/aya31/Desktop/M1 MIASHS/M1S2/WePlant_25.5"  # <-- ton dossier
INDEX_NAME = "mon-index"                                       # déjà créé
NAMESPACE = "default"                                          # tu peux changer
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"          # 384 dims
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
BATCH_SIZE = 100

# Extensions texte à EMBED (code + docs)
TEXT_EXTS = {
    ".py", ".ipynb", ".r", ".sql",
    ".js", ".ts", ".jsx", ".tsx",
    ".java", ".c", ".cpp",
    ".md", ".txt", ".qmd", ".rmd", ".rst"
}
# Dossiers à ignorer
IGNORE_DIRS = {".git", "__pycache__", ".ipynb_checkpoints", "node_modules", "build", "dist", ".DS_Store", ".venv", "venv"}

# ---- IMPORTS LIBS ----
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
import numpy as np

# ---- UTILS ----
def iter_text_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            # ignorer fichiers cachés et binaires courants
            if fn.startswith("."): 
                continue
            ext = p.suffix.lower()
            if ext in TEXT_EXTS:
                yield p

def read_text(p: Path) -> str:
    ext = p.suffix.lower()
    try:
        if ext == ".ipynb":
            import json as _json
            nb = _json.loads(p.read_text(encoding="utf-8", errors="ignore"))
            cells = nb.get("cells", [])
            parts = []
            for c in cells:
                src = c.get("source", [])
                if isinstance(src, list):
                    parts.append("".join(src))
                else:
                    parts.append(str(src))
            return "\n".join(parts)
        else:
            return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def chunk_text(text: str, max_chars=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    text = text.strip()
    if not text:
        return []
    chunks = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + max_chars, n)
        chunks.append(text[start:end])
        if end == n:
            break
        start = max(0, end - overlap)
    return chunks

def main():
    # 1) Modèle d'embeddings
    print(f"[INFO] Chargement du modèle: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)  # 384 dims

    # 2) Pinecone
    api_key = os.environ.get("PINECONE_API_KEY") or "REMPLACE_MOI"
    if api_key == "REMPLACE_MOI":
        raise ValueError("Définis la variable d'environnement PINECONE_API_KEY")
    pc = Pinecone(api_key=api_key)
    index = pc.Index(INDEX_NAME)

    # 3) Itération fichiers → chunks → embeddings → upsert(batch)
    to_upsert = []
    total_chunks = 0

    for file_path in iter_text_files(ROOT_DIR):
        text = read_text(file_path)
        if not text:
            continue
        chunks = chunk_text(text)
        if not chunks:
            continue

        # embeddings (normalisés par défaut avec ST ? on utilise cosine au query côté index)
        embs = model.encode(chunks, normalize_embeddings=True)

        # préparer les vecteurs à upsert
        for i, (ch, vec) in enumerate(zip(chunks, embs)):
            vid = f"{file_path.as_posix()}::chunk_{i}"
            meta = {
                "file": file_path.as_posix(),
                "chunk_id": i,
                "type": "code" if file_path.suffix.lower() not in {".md", ".txt", ".qmd", ".rmd", ".rst"} else "doc",
                "text": ch[:2000]  # stocker un extrait (éviter trop gros)
            }
            to_upsert.append({
                "id": vid,
                "values": vec.astype("float32").tolist(),
                "metadata": meta
            })

            # batch
            if len(to_upsert) >= BATCH_SIZE:
                index.upsert(vectors=to_upsert, namespace=NAMESPACE)
                to_upsert = []
                # petite pause pour la propagation
                time.sleep(0.2)

        total_chunks += len(chunks)
        print(f"[OK] {file_path} → {len(chunks)} chunks (total: {total_chunks})")

    # dernier batch
    if to_upsert:
        index.upsert(vectors=to_upsert, namespace=NAMESPACE)

    # attendre un peu puis test
    time.sleep(2)
    # petit test: requête sur un terme du projet
    q = "Comment fonctionne la recommandation de plantes ?"
    qvec = model.encode([q], normalize_embeddings=True)[0].astype("float32").tolist()
    res = index.query(vector=qvec, top_k=5, include_metadata=True, namespace=NAMESPACE)
    print("\n[TEST QUERY] →", q)
    for m in res.get("matches", []):
        print(f"score={m['score']:.3f} | {m['metadata'].get('file')} | chunk={m['metadata'].get('chunk_id')}")

    print(f"\n[FIN] {total_chunks} chunks envoyés dans l'index '{INDEX_NAME}' (namespace='{NAMESPACE}').")

if __name__ == "__main__":
    main()
