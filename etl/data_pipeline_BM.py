from ingestion import load_event_data
from transformation import clean_event_data, calculate_kpis
from loading import load_to_sqlite
import os

def run_pipeline(file_path):
    print("______________________Ingestion______________________")
    df = load_event_data(file_path)
    print("Raw Data Sample:")
    print(df.head())

    print("______________________Transformation______________________")
    df_clean = clean_event_data(df)
    print("Cleaned Data Sample:")
    print(df_clean.head())
    kpis = calculate_kpis(df_clean)
    ("Calculated KPIs:")
    print(kpis)
    print("______________________Loading to database______________________")
    conn = load_to_sqlite(kpis)
    print("______________________ETL complete. Database ready.______________________")
    return conn

if __name__ == "__main__":

    directory ='/opt/airflow/data/events/'
    for f in os.listdir(directory) :
        if f.endswith('.json') :
            conn = run_pipeline(directory+ f)
