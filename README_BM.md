# ⚽ Monaco Test technique (Tache 1): Football Team Name Standardization 🧹

*Un script pour nettoyer et standardiser les noms d'équipes de football provenant de différentes sources*

---

## 🎯 Objectif

Ce script permet de **harmoniser les noms d'équipes** qui peuvent varier selon les sources de données. Par exemple :  
- `Al-Nassr FC` (Source 1)  
- `Nassr` (Source 2)  
- `Al-Nassr` (Source 3)  

➡ Tous deviennent **`Al-Nassr FC`** (nom standardisé)

---

## 📦 Dépendances & Exécution

1. **Cloner le dépôt**

```bash
git clone https://github.com/mbirame2/test_technique/tree/taskone
```

2. **Installation dépendances**

```bash
pip install pandas fuzzywuzzy  
```

3. **Tester le script**

```bash
python team_name_cleaning_BM.py  
```

---

## 📂 Fichiers
- `team_name_cleaning_BM.py` : Script principal
- `data/file_ASM.xlsx` : Fichier d entrée (données brutes)
- `cleaned_teams_BM.xlsx` : Résultat final (généré automatiquement)

## 🛠 Fonctionnement du code

### 🔧 1. Nettoyage des noms (`clean_name()`)

### 🧩 2. Regroupement des équipes (standardize_team_names())
-   Récupère tous les noms uniques ✅
-   Compare chaque paire avec fuzzy matching 🤝
-   Crée des groupes quand la similarité > 85% 🔄

### 🎯 3. Choix du nom standard
-   Prend le nom le plus long dans chaque groupe (Plus complet et descriptif) 📏

---

---

## 📦 Test

```bash
python team_name_cleaning_BM.py  
```

---

## 🎯 Résultatss :

Un nouveau fichier Excel est créé (cleaned_teams_BM.xlsx)

Contient la colonne standard_team_name 🆕

