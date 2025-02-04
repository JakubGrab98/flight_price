import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def fetch_api_data():
    sys.path.append('/opt/airflow/jobs')
    from fetch_api import main
    main()


with DAG("flight_flow",
         default_args={
        "owner": "Jakub Grabarczyk",
        "start_date": datetime(2025, 1, 12),
        "provide_context": True,
    },
    schedule_interval="@daily",
) as dag:

    extract_api_data = PythonOperator(
        task_id="extract_data",
        python_callable=fetch_api_data,
    )

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='docker exec dbt_container dbt run'
    )

    extract_api_data >> dbt_run