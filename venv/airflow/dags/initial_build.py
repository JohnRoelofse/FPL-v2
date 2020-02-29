import sys
sys.path.insert(1, '/home/ubuntu/venv/python_scripts/functions/')

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from populate_initial_tables import populate_initial_tables
from create_tables import create_tables

default_args = {
        'owner': 'John',
        'start_date': datetime(2019,1,1),
        }

dag = DAG('initial_build', default_args=default_args)

create_tables = PythonOperator(
        task_id='create_tables',
        dag=dag,
        python_callable=create_tables,
        schedule_interval='@Once')

populate_tables = PythonOperator(
        task_id='populate_tables',
        dag=dag,
        python_callable=populate_initial_tables,
        schedule_interval='@Once'
        )

create_tables >> populate_tables