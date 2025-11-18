# **TEST2 - Projet d'Analyse et de Manipulation de Données**

## **Présentation générale**
Ce projet **TEST2** est un ensemble de scripts Python et notebooks Jupyter conçus pour :
- **Manipuler des données** (CSV, DataFrames pandas)
- **Effectuer des calculs mathématiques** (numpy)
- **Visualiser des données** (matplotlib)
- **Gérer des fichiers et dossiers** (os)
- **Automatiser des tâches simples** (compter des lignes, créer des DataFrames)

Le projet est organisé en plusieurs dossiers et fichiers, chacun ayant un rôle spécifique.

---

## **Arborescence du dossier**
```
TEST2/
│
├── code3.py          # Script principal avec fonctions de base
├── data2.csv         # Fichier CSV de données
│
├── DOSSIER 1/
│   ├── code1.py      # Fonctions mathématiques et utilitaires
│   ├── code5.ipynb   # Notebook Jupyter pour visualisation
│   ├── data.csv      # Fichier CSV de données
│   └── test1.txt     # Fichier texte de test
│
└── DOSSIER 2/
    ├── code2.py      # Fonctions de gestion de fichiers
    ├── code4.ipynb   # Notebook Jupyter pour analyse
    └── test2.docx    # Document Word de test
```

---

## **Bibliothèques nécessaires**
Pour exécuter ce projet, installez les dépendances suivantes :
```bash
pip install pandas numpy matplotlib
```

---

## **Fonctionnement global**
1. **Manipulation de données** :
   - `code1.py` et `code3.py` contiennent des fonctions pour créer et manipuler des DataFrames pandas.
   - `data.csv` et `data2.csv` sont utilisés pour le traitement des données.

2. **Calculs mathématiques** :
   - `code1.py` inclut des fonctions comme `sqrt`, `factorial`, et `add`.
   - `code3.py` génère des DataFrames aléatoires.

3. **Visualisation** :
   - `code5.ipynb` et `code4.ipynb` utilisent `matplotlib` pour tracer des graphiques.

4. **Gestion de fichiers** :
   - `code2.py` permet de lister, créer et lire des fichiers/dossiers.

---

## **Résumé fichier par fichier**

### **Fichiers principaux**
- **`code3.py`** :
  - Fonctions pour générer des DataFrames aléatoires (`example_function`).
  - Fonctions mathématiques (`another_function`, `yet_another_function`).

- **`data2.csv`** :
  - Fichier CSV contenant des données brutes.

### **DOSSIER 1**
- **`code1.py`** :
  - Fonctions mathématiques (`add`, `multiply`, `divide`, `subtract`, `factorial`).
  - Fonction `hello_world()` pour un test simple.

- **`code5.ipynb`** :
  - Notebook Jupyter pour visualiser des données avec `matplotlib`.

- **`data.csv`** :
  - Fichier CSV utilisé pour l'analyse.

- **`test1.txt`** :
  - Fichier texte de test.

### **DOSSIER 2**
- **`code2.py`** :
  - Fonctions pour gérer des fichiers (`list_files`, `create_folder`, `create_file`, `read_file`).

- **`code4.ipynb`** :
  - Notebook Jupyter pour analyser des données.

- **`test2.docx`** :
  - Document Word de test.

---

## **Comment lancer le projet**
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/TEST2.git
   cd TEST2
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter les scripts** :
   - Pour `code3.py` :
     ```bash
     python code3.py
     ```
   - Pour `code1.py` :
     ```bash
     python DOSSIER1/code1.py
     ```
   - Pour `code2.py` :
     ```bash
     python DOSSIER2/code2.py
     ```

4. **Lancer les notebooks Jupyter** :
   ```bash
   jupyter notebook DOSSIER1/code5.ipynb
   jupyter notebook DOSSIER2/code4.ipynb
   ```

---

## **Conclusion**
Ce projet est un ensemble de scripts Python et notebooks Jupyter pour :
✅ **Manipuler des données** (pandas, numpy)
✅ **Visualiser des données** (matplotlib)
✅ **Gérer des fichiers** (os)
✅ **Automatiser des tâches simples**

Il est idéal pour des tâches de **data analysis**, **automatisation** et **visualisation rapide**.

---

**Auteur** : [Votre Nom]
**Date** : [Date]
**Version** : 1.0