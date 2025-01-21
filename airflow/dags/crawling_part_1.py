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
    'start_date': datetime(2025, 1, 17, tzinfo=local_tz),
}

with DAG(
    dag_id='run_crawling_script',
    default_args=default_args,
    concurrency=1,
    schedule_interval='@daily',
    catchup=False,
    tags=['crawling', 'daily']
) as dag:

    crawling_kt = BashOperator(
        task_id='run_crawling_kt',
        bash_command='python3 /opt/airflow/projects/crawling/kt.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_hyundai_tv = BashOperator(
        task_id='run_crawling_hyundai_tv',
        bash_command='python3 /opt/airflow/projects/crawling/hyundai_tv.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_lotte_llive = BashOperator(
        task_id='run_crawling_lotte_llive.py',
        bash_command='python3 /opt/airflow/projects/crawling/lotte_llive.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_lotte = BashOperator(
        task_id='run_crawling_lotte',
        bash_command='python3 /opt/airflow/projects/crawling/lotte.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )
    
    crawling_sk = BashOperator(
        task_id='run_crawling_sk',
        bash_command='python3 /opt/airflow/projects/crawling/sk.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )


    crawling_w_home = BashOperator(
        task_id='run_crawling_w_home',
        bash_command='python3 /opt/airflow/projects/crawling/w_home.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_kt >> crawling_hyundai_tv >> crawling_lotte_llive >> crawling_lotte >> crawling_sk >> crawling_w_home
