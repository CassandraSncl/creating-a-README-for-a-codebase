# Projet TEST2

## Présentation générale
Ce projet est un ensemble de scripts Python et notebooks Jupyter conçus pour effectuer diverses opérations de traitement de données, de manipulation de fichiers et de visualisation. Il inclut des fonctions pour la création et la manipulation de DataFrames, des opérations mathématiques de base, ainsi que des outils pour la gestion de fichiers et dossiers.

## Arborescence du dossier
```
TEST2/
    code3.py          # Script principal avec fonctions de traitement de données
    data2.csv         # Fichier de données CSV
    DOSSIER 1/
        code1.py      # Script avec fonctions de manipulation de fichiers
        code5.ipynb   # Notebook Jupyter pour l'analyse de données
        data.csv      # Fichier de données CSV
        test1.txt     # Fichier texte de test
    DOSSIER 2/
        code2.py      # Script avec fonctions mathématiques
        code4.ipynb   # Notebook Jupyter pour la visualisation
        test2.docx    # Document Word de test
```

## Bibliothèques nécessaires
- Python 3.7+
- pandas
- numpy
- matplotlib
- os (standard library)
- jupyter (pour exécuter les notebooks)

Installez les dépendances avec:
```bash
pip install pandas numpy matplotlib jupyter
```

## Fonctionnement global
Le projet est organisé autour de plusieurs modules qui fournissent des fonctionnalités spécifiques:
1. **Manipulation de données**: Création et traitement de DataFrames
2. **Opérations mathématiques**: Fonctions de base et calculs avancés
3. **Gestion de fichiers**: Lecture, écriture et manipulation de fichiers
4. **Visualisation**: Création de graphiques simples

## Résumé fichier par fichier

### code3.py
Contient des fonctions pour la création et le traitement de DataFrames:
- `example_function()`: Crée un DataFrame avec des valeurs aléatoires
- `another_function(x)`: Calcule la racine carrée d'un nombre
- `yet_another_function(lst)`: Double chaque élément d'une liste

### data2.csv
Fichier de données CSV principal utilisé par le projet.

### DOSSIER 1/code1.py
Script de gestion de fichiers avec:
- `list_files(folder)`: Liste les fichiers dans un dossier
- `create_folder(folder)`: Crée un dossier s'il n'existe pas
- `create_file(path, content)`: Crée un fichier avec du contenu
- `read_file(path)`: Lit le contenu d'un fichier

### DOSSIER 1/code5.ipynb
Notebook Jupyter pour l'analyse de données contenant:
- Importation de données
- Nettoyage et transformation
- Visualisation des résultats

### DOSSIER 1/data.csv
Fichier de données CSV utilisé par le notebook code5.ipynb.

### DOSSIER 1/test1.txt
Fichier texte de test pour les opérations de lecture/écriture.

### DOSSIER 2/code2.py
Script avec fonctions mathématiques:
- `hello_world()`: Affiche "Hello world!"
- `add(a, b)`: Additionne deux nombres
- `multiply(a, b)`: Multiplie deux nombres
- `divide(a, b)`: Divise deux nombres (avec gestion de la division par zéro)
- `subtract(a, b)`: Soustrait deux nombres
- `factorial(n)`: Calcule la factorielle d'un nombre

### DOSSIER 2/code4.ipynb
Notebook Jupyter pour la visualisation contenant:
- Création de graphiques avec matplotlib
- Visualisation de données simples

### DOSSIER 2/test2.docx
Document Word de test pour les opérations de gestion de fichiers.

## Comment lancer le projet

1. **Installer les dépendances**:
   ```bash
   pip install pandas numpy matplotlib jupyter
   ```

2. **Exécuter les scripts**:
   - Pour code3.py:
     ```bash
     python code3.py
     ```
   - Pour code1.py:
     ```bash
     python DOSSIER1/code1.py
     ```
   - Pour code2.py:
     ```bash
     python DOSSIER2/code2.py
     ```

3. **Lancer les notebooks**:
   ```bash
   jupyter notebook
   ```
   Puis ouvrez les notebooks code5.ipynb et code4.ipynb dans l'interface Jupyter.

4. **Utilisation des fonctions**:
   Importez les fonctions dans vos scripts Python:
   ```python
   from code3 import example_function
   from DOSSIER1.code1 import list_files
   from DOSSIER2.code2 import add
   ```

## Notes supplémentaires
- Assurez-vous que tous les fichiers de données sont présents dans leurs emplacements respectifs
- Les notebooks Jupyter nécessitent Jupyter Notebook ou JupyterLab installé
- Pour les opérations de gestion de fichiers, vérifiez les permissions d'accès aux dossiers et fichiers