# Titre du projet
README Generator avec RAG

# Lien vidéo démonstration
https://drive.google.com/file/d/1IQsLtyoSV6eSy1exc-zqx1qoDBClNoFW/view?usp=sharing


# Présentation générale et fonctionnement
Ce projet est un outil d'analyse de code qui génère automatiquement un fichier README.md pour un projet donné. Il utilise une approche RAG (Retrieval-Augmented Generation) pour analyser le code source, créer des embeddings avec un modèle d'embeddings, et générer une documentation structurée. Le système lit les fichiers de code, les découpe en chunks logiques, les vectorise, et utilise un LLM pour produire un README professionnel.

# Arborescence du projet des fichiers importants
```
creating-a-README-for-a-codebase/
CREATE_README.ipynb
TESTS/
    embeddings.ipynb
    embeddings2.ipynb
    embed_folder_to_pinecone.py
    show_tree.ipynb
    TEST2/
        code3.py
        DOSSIER 1/
            code1.py
            code5.ipynb
        DOSSIER 2/
            code2.py
            code4.ipynb
    TEST_FUNCTIONS/
        code1.py
        code2.py
        code3.ipynb
VERSIONS/
    create_readme.ipynb
    create_readme_chunks.ipynb
    create_readme_final.ipynb
    create_readme_RAG.ipynb
    CREATE_README_V1.ipynb
```

# Bibliothèques nécessaires pour le projet
- os
- json
- re
- numpy
- time
- random
- concurrent.futures
- faiss
- sentence_transformers
- pinecone
- pathlib
- matplotlib
- pandas

# Résumé catégories par catégories

## Scripts principaux
- `CREATE_README.ipynb`: Point d'entrée principal pour générer le README
- `create_readme_RAG.ipynb`: Implémentation du pipeline RAG complet
- `embed_folder_to_pinecone.py`: Script pour indexer le code dans Pinecone

## Modules d'analyse
- `show_tree.ipynb`: Fonctions pour afficher l'arborescence du projet
- `embeddings.ipynb`/`embeddings2.ipynb`: Fonctions pour créer et gérer les embeddings
- `code1.py`/`code2.py`/`code3.py`: Scripts de test et exemples de code

## Fonctionnalités clés
- Lecture récursive des fichiers de code (.py, .ipynb)
- Découpage intelligent en chunks (par fonctions, par taille)
- Création d'embeddings avec gestion des erreurs 429
- Indexation dans FAISS ou Pinecone
- Génération de documentation via LLM

# Comment lancer le projet
1. Installez les dépendances requises:
```bash
pip install numpy faiss-cpu sentence-transformers pinecone-client pandas matplotlib
```

2. Configurez les variables d'environnement:
```bash
export MISTRAL_API_KEY="votre_clé_api"
```

3. Exécutez le script principal:
```bash
python CREATE_README.ipynb
```

4. Entrez le chemin du dossier à analyser lorsque demandé

### Avertissements et limitations
- Le projet nécessite une clé API valide pour Pinecone
- Les performances dépendent de la taille du projet analysé
- La qualité du README généré dépend de la qualité du code source
- Certains fichiers système ou de configuration peuvent être ignorés
- Le processus peut prendre du temps pour les projets volumineux