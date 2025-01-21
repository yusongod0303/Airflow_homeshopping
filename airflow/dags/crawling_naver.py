from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime
import pendulum

local_tz = pendulum.timezone("Asia/Seoul")

AIRFLOW_USER = Variable.get("AIRFLOW_USER", default_var="airflow")

default_args = {
    'owner': AIRFLOW_USER,
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 21, tzinfo=local_tz),
}

with DAG(
    dag_id='run_crawling_naver_trend',
    default_args=default_args,
    concurrency=1,
    schedule_interval='@daily',
    catchup=False,
    tags=['crawling', 'daily', 'naver']
) as dag:

    crawling_kt = BashOperator(
        task_id='run_crawling_naver',
        bash_command='python3 /opt/airflow/projects/crawling/naver_rank.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )
