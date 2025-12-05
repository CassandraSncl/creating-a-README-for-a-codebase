# Titre du projet
README Generator

# Lien vidéo démonstration
https://drive.google.com/file/d/1IQsLtyoSV6eSy1exc-zqx1qoDBClNoFW/view?usp=sharing


# Présentation générale et fonctionnement
Ce projet est un outil d'analyse de code qui génère automatiquement un fichier README.md pour un projet donné. Il utilise une approche RAG (Retrieval-Augmented Generation) pour analyser le code source, créer des embeddings avec un modèle d'embeddings, et générer une documentation structurée. Le système lit les fichiers de code, les découpe en chunks logiques, les vectorise, et utilise un LLM pour produire un README professionnel.

L'outil fonctionne en plusieurs étapes :
1. Analyse de l'arborescence du projet
2. Extraction et chunking du code
3. Génération d'embeddings vectoriels
4. Création d'un index FAISS pour la recherche de similarité
5. Génération du README via un LLM (Codestral)

Le projet est particulièrement utile pour les développeurs qui souhaitent documenter rapidement des projets sans avoir à écrire manuellement des README détaillés.

# Arborescence du projet des fichiers importants
```
creating-a-README-for-a-codebase/
    CREATE_README.ipynb
    OLD-VERSIONS/
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
- faiss
- random
- time
- concurrent.futures

# Résumé catégories par catégories

## Scripts principaux
- `CREATE_README.ipynb` : Script principal pour générer le README
- `OLD-VERSIONS/` : Dossier contenant différentes versions du projet

## Fonctionnalités clés
- `show_tree()` : Génère une arborescence synthétique du projet
- `read_code()` : Lit et extrait le code des fichiers
- `split_functions()` : Découpe le code en fonctions/chunks
- `create_embeddings()` : Génère des embeddings vectoriels
- `generate_readme_RAG()` : Pipeline complet de génération du README

## Fonctionnalités techniques
- Gestion des erreurs pour les appels API
- Chunking intelligent avec découpage par fonctions
- Indexation FAISS pour la recherche de similarité
- Parallélisation des opérations I/O

# Comment lancer le projet
1. Installez les dépendances nécessaires :
```bash
pip install numpy faiss-cpu
 ```

2. Exécutez le script principal :
```bash
   jupyter notebook CREATE_README.ipynb
```

3. Entrez le chemin du dossier à analyser lorsque demandé

4. Le README sera généré dans le dossier spécifié

> Informations à compléter : Vérifiez que toutes les dépendances sont installées et que le chemin du dossier est correct.

### Avertissements et limitations
- Le projet nécessite une connexion Internet pour les appels API
- Les performances dépendent de la taille du projet analysé
- La qualité du README généré dépend de la qualité du code source
- Certaines sections peuvent nécessiter des ajustements manuels
- Le projet est actuellement optimisé pour Python et notebooks Jupyter