from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime, timedelta

AIRFLOW_USER = Variable.get("AIRFLOW_USER", default_var="airflow")
GITHUB_USER = Variable.get("GITHUB_USER")
GITHUB_TOKEN = Variable.get("GITHUB_TOKEN")
PROJECT_DIR = "/opt/airflow/projects/crawling"
WEB_PROJECT_DIR = "/opt/airflow/projects/last_pj_web"

default_args = {
    'owner': AIRFLOW_USER,
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='git_pull_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['github', 'crawling', 'web'],
) as dag:
    # crawling 프로젝트 PULL
    git_pull_crawling_task = BashOperator(
        task_id='git_pull_crawling',
        bash_command=f"""
        ls -la {PROJECT_DIR}
        cd {PROJECT_DIR}
        git fetch origin
        git reset --hard origin/main
        git pull https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/crawling.git main
        """,
    )

    # web 프로젝트 PULL
    git_pull_web_task = BashOperator(
        task_id='git_pull_web',
        bash_command=f"""
        ls -la {WEB_PROJECT_DIR}
        cd {WEB_PROJECT_DIR}
        git fetch origin
        git reset --hard origin/main
        git pull https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/last_pj_web.git main
        """,
    )

    git_pull_crawling_task >> git_pull_web_task
