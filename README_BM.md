
# README_XX.md

# ⚽ Projet ETL StatsBomb avec Apache Airflow et Docker 🐳

---

## 📋 Description

Ce projet est un pipeline ETL (Extract, Transform, Load) pour analyser des données footballistiques issues de StatsBomb.  
Le pipeline permet d'ingérer les fichiers JSON d'événements, de transformer les données pour calculer des KPI (indicateurs de performance clés) comme la précision de passe, la possession, le taux de conversion de tirs, puis de charger ces résultats dans une base SQLite.

Le workflow est orchestré avec Apache Airflow, déployé dans des containers Docker pour assurer modularité, portabilité et reproductibilité.

---

## 🏗️ Architecture technique

- **Apache Airflow** : orchestrateur des tâches ETL, permet de planifier et monitorer les DAGs (pipelines). ⏰
- **Docker** : containerisation de l’ensemble (Airflow, PostgreSQL pour Airflow metadata, ETL Python). 🐳
- **PostgreSQL** : base de données utilisée par Airflow pour stocker ses métadonnées. 🗄️
- **SQLite** : base légère utilisée pour stocker les données transformées et les KPI calculés. 💾
- **Python** : pour le développement des scripts ETL (ingestion, transformation, chargement). 🐍
- **BashOperator + DockerOperator dans Airflow** : exécution du script ETL dans un container dédié. ⚙️

---

## 📝 Choix techniques

- Utilisation de **Docker Compose** pour faciliter le déploiement local complet (Airflow + Postgres + ETL).  
- **LocalExecutor** d’Airflow pour une orchestration simple sur une seule machine.  
- **DockerOperator** dans Airflow pour isoler l’exécution ETL dans un container dédié, garantissant la reproductibilité et l’isolation des dépendances.  
- Base SQLite légère pour la persistance des KPI, facile à consulter et copier hors du container.  
- Gestion des connexions Airflow via variables d’environnement dans Docker Compose pour simplifier la configuration.  
- Planification du DAG en mode cron (ex: toutes les 5 minutes) pour un monitoring et une exécution régulière. ⏳

---

## ⚙️ Prérequis

- Docker & Docker Compose installés et fonctionnels  
- Accès terminal / ligne de commande

---

## 🚀 Installation & Exécution

1. **Cloner le dépôt**

```bash
git clone <url-du-projet>
cd <nom-du-projet>
```

2. **Construire l’image ETL**

```bash
docker-compose build etl
```

3. **Démarrer la stack**

```bash
docker-compose up -d
```

4. **Initialiser la base de données Airflow** (à faire une seule fois)

```bash
docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
    --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

5. **Lancer les services**

```bash
docker-compose start airflow-webserver airflow-scheduler postgres
```

6. **Accéder à l’interface Airflow**

Ouvrir dans un navigateur :  
[http://localhost:8080](http://localhost:8080)  
Login : `admin` / `admin` 🔐

7. **Déclencher et monitorer le DAG** `statsbomb_etl_pipeline`  
- Le DAG est configuré pour s’exécuter toutes les 5 minutes ⏲️  
- Visualiser les logs des tâches dans l’UI Airflow 📊

---

## 📁 Structure des dossiers

```
├── dags/                # Contient les fichiers DAG Airflow
│   └── etl_pipeline_dag.py
├── etl/                 # Code source des scripts ETL
│   ├── ingestion.py
│   ├── transformation.py
│   ├── loading.py
│   └── data_pipeline_BM.py
├── data/                # Données statiques ou d’exemple (JSON)
├── Dockerfile           # Image custom pour le pipeline ETL
├── docker-compose.yml   # Orchestration des containers
├── requirements.txt     # Dépendances Python
└── README_XX.md         # Ce fichier
```

---

## 🛠️ Debug & Conseils

- Pour accéder à la base SQLite générée, récupérer le fichier `.db` dans le container ETL via `docker cp`.  
- Pour afficher les tables SQLite :  
  ```bash
  sqlite3 <database_file>.db
  .tables
  ```  
- Assurez-vous que les volumes Docker sont bien montés pour persister les données.  
- En cas de problème de démarrage Airflow, vérifier que la DB Postgres est accessible et que la migration est effectuée (`airflow db init` / `airflow db migrate`).  

---

N’hésitez pas à me demander si vous souhaitez un exemple plus complet ou un fichier adapté à votre besoin ! 😊
