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
    dag_id='run_crawling_script_part2',
    default_args=default_args,
    concurrency=1,
    schedule_interval='@daily',
    catchup=False,

    tags=['crawling', 'daily', 'part2']
) as dag:

    crawling_cj_plus = BashOperator(
        task_id='run_crawling_cj_plus',
        bash_command='python3 /opt/airflow/projects/crawling/cj_plus.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_cj_tv = BashOperator(
        task_id='run_crawling_cj_tv',
        bash_command='python3 /opt/airflow/projects/crawling/cj_tv.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_gongyoung = BashOperator(
        task_id='run_crawling_gongyoung',
        bash_command='python3 /opt/airflow/projects/crawling/gongyoung.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_GS_shop_live = BashOperator(
        task_id='run_crawling_GS_shop_live',
        bash_command='python3 /opt/airflow/projects/crawling/GS_shop_live.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_GS_tv = BashOperator(
        task_id='run_crawling_GS_tv',
        bash_command='python3 /opt/airflow/projects/crawling/GS_tv.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_home_and_shop = BashOperator(
        task_id='run_crawling_home_and_shop',
        bash_command='python3 /opt/airflow/projects/crawling/home_and_shop.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_hyundai_plus = BashOperator(
        task_id='run_crawling_hyundai_plus',
        bash_command='python3 /opt/airflow/projects/crawling/hyundai_plus.py',
        env={
            'PATH':'/opt/airflow/chromedriver-linux64:/opt/airflow/chrome-linux64:/usr/local/bin:${PATH}'
        }
    )

    crawling_cj_plus >> crawling_cj_tv >> crawling_gongyoung >> crawling_GS_shop_live >> crawling_GS_tv >> crawling_home_and_shop >> crawling_hyundai_plus 
