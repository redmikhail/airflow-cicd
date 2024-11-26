from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print(‘Hello World’)
          
with DAG(dag_id="hello_world_dag",
         start_date=datetime(2021,1,1),
         schedule_interval="@once",
         catchup=False
) as dag:
    print_hello_world = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld
    )
    print_hello_world