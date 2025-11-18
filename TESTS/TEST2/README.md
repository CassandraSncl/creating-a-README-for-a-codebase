# **Projet TEST2**

## **Présentation générale**
Le projet **TEST2** est un ensemble de scripts Python et notebooks Jupyter conçus pour effectuer des opérations de traitement de données, de visualisation et de manipulation de fichiers. Il inclut des fonctions pour la création et la manipulation de DataFrames, des calculs mathématiques, ainsi que des outils pour gérer des fichiers et dossiers.

Le projet est organisé en plusieurs modules répartis dans des dossiers distincts, chacun ayant un rôle spécifique.

---

## **Arborescence du dossier**
```
TEST2/
│
├── code3.py                # Script principal avec des fonctions de traitement de données
├── data2.csv               # Fichier CSV de données
│
├── DOSSIER 1/              # Module de traitement de données et visualisation
│   ├── code1.py            # Fonctions de génération de DataFrames et calculs
│   ├── code5.ipynb         # Notebook Jupyter pour l'analyse de données
│   ├── data.csv            # Fichier CSV de données
│   └── test1.txt           # Fichier texte de test
│
├── DOSSIER 2/              # Module de gestion de fichiers et calculs mathématiques
│   ├── code2.py            # Fonctions de gestion de fichiers et dossiers
│   └── code4.ipynb         # Notebook Jupyter pour des calculs et visualisations
│   └── test2.docx         # Document Word de test
│
```

---

## **Bibliothèques nécessaires**
Pour exécuter ce projet, installez les dépendances suivantes :
```bash
pip install pandas numpy matplotlib
```

---

## **Fonctionnement global**
Le projet est structuré en plusieurs modules :
1. **`DOSSIER 1`** : Contient des fonctions pour la génération de DataFrames, l'analyse de données et la visualisation.
2. **`DOSSIER 2`** : Gère les opérations de gestion de fichiers et dossiers, ainsi que des calculs mathématiques.
3. **Scripts principaux** : `code3.py` et `code2.py` fournissent des fonctions utilitaires pour le traitement de données et la manipulation de fichiers.

---

## **Résumé fichier par fichier**

### **`code3.py`**
- **Fonctions principales** :
  - `example_function()` : Génère un DataFrame aléatoire avec des colonnes `A`, `B`, `C`.
  - `another_function(x)` : Calcule la racine carrée d'un nombre.
  - `yet_another_function(lst)` : Double chaque élément d'une liste.

### **`DOSSIER 1/code1.py`**
- **Fonctions principales** :
  - `create_dataframe(list_letters, list_numbers=None)` : Crée un DataFrame à partir de listes de lettres et de nombres.
  - `count_lines(file_path)` : Compte le nombre de lignes dans un fichier.

### **`DOSSIER 1/code5.ipynb`**
- **Contenu** : Notebook Jupyter pour l'analyse de données, probablement lié à `data.csv`.

### **`DOSSIER 2/code2.py`**
- **Fonctions principales** :
  - `list_files(folder)` : Liste les fichiers dans un dossier.
  - `create_folder(folder)` : Crée un dossier s'il n'existe pas.
  - `create_file(path, content)` : Crée un fichier avec un contenu donné.
  - `read_file(path)` : Lit le contenu d'un fichier.

### **`DOSSIER 2/code4.ipynb`**
- **Contenu** : Notebook Jupyter pour des calculs et visualisations (ex. `matplotlib`).

---

## **Comment lancer le projet**
1. **Cloner le dépôt** :
   ```bash
   git clone <url-du-projet>
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
   - Pour `DOSSIER 1/code1.py` :
     ```bash
     python DOSSIER\ 1/code1.py
     ```
   - Pour `DOSSIER 2/code2.py` :
     ```bash
     python DOSSIER\ 2/code2.py
     ```

4. **Lancer les notebooks Jupyter** :
   ```bash
   jupyter notebook
   ```
   Puis ouvrir `DOSSIER 1/code5.ipynb` et `DOSSIER 2/code4.ipynb`.

---

## **Conclusion**
Ce projet est un ensemble de scripts Python et notebooks Jupyter pour le traitement de données, la visualisation et la gestion de fichiers. Il est modulaire et peut être étendu pour des applications plus complexes.

**Auteur** : [Votre nom]
**Date** : [Date de création]