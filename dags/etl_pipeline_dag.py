from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'statsbomb',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('statsbomb_etl_pipeline',
         default_args=default_args,
         schedule_interval='*/10 * * * *',
         catchup=False,
         description='ETL pipeline to compute football KPIs',
         tags=['statsbomb', 'football'],
         ) as dag:

    run_etl = BashOperator(
        task_id='run_etl_script',
        bash_command='python /opt/airflow/etl/data_pipeline_BM.py'
    )

    run_etl
