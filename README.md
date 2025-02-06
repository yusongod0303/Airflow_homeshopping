# Airflow 데이터 파이프라인 프로젝트

## 프로젝트 개요
이 프로젝트는 Apache Airflow를 활용해 데이터 수집, 변환, 적재(ETL) 작업을 자동화하고, 작업 상태를 모니터링하는 데이터 파이프라인을 설계하기 위해 만들어졌습니다.

- **주요 목적**: 대규모 데이터 처리 및 자동화를 통해 데이터 워크플로우를 최적화
- **기술 스택**:
  - **Apache Airflow**: 워크플로우 오케스트레이션
  - **Docker**: 컨테이너 기반 배포
  - **PostgreSQL**: 메타데이터 저장소
  - **Redis**: 메시지 브로커
  - **EC2 (Amazon Linux)**: 프로젝트 호스팅

---

## 주요 기능
1. **데이터 수집**:
   - 다양한 소스(예: API, 웹 크롤러 등)에서 데이터를 수집하는 태스크 포함.
2. **데이터 변환**:
   - 원시 데이터를 정제하고, 분석 가능한 형태로 가공.
3. **데이터 적재**:
   - 변환된 데이터를 데이터베이스 또는 스토리지로 저장.
4. **스케줄링**:
   - 데이터 파이프라인 작업을 매일 자동으로 실행하도록 설정.
5. **모니터링**:
   - Airflow 웹 UI를 통해 DAG 실행 상태와 태스크 로그를 실시간으로 확인 가능.

---

## 디렉토리 구조
├── README.md  
├── docker-compose.yaml  
├── .gitignore  
├── airflow/  
│   ├── dags/  
│   │   ├── crawling_naver.py  
│   │   ├── crawling_part_1.py  
│   │   ├── crawling_part_2.py  
│   │   └── git_pull.py  
│   ├── plugins/  
│   ├── images/  
    └── ys-airflow/  
        ├── Dockerfile  
        └── build_docker.sh  
│   └── logs/  
├── projects/  
│   ├── crawling/  
│   │   ├── GS_shop_live.py  
│   │   ├── GS_tv.py  
│   │   ├── NS_plus.py  
│   │   ├── NS_tv.py  
│   │   ├── cj_plus.py  
│   │   ├── cj_tv.py  
│   │   ├── gongyoung.py  
│   │   ├── home_and_shop.py  
│   │   ├── hyundai_plus.py  
│   │   ├── hyundai_tv.py  
│   │   ├── kt.py  
│   │   ├── lotte.py  
│   │   ├── lotte_llive.py  
│   │   ├── naver_rank.py  
│   │   ├── shop_enti.py  
│   │   ├── sk.py  
│   │   ├── ssg.py  
│   │   └── w_home.py  
│   │   
│   └── last_pj_web/  
        ├── main.py  
        ├── test.py  
        └── templates/  
            ├── detail.html  
            ├── edit.html  
            ├── favorite.html  
            ├── index.html  
            ├── login.html  
            ├── main.html  
            ├── myinfo.html  
            ├── schedule.html  
            ├── search.html  
            ├── signup.html  
            ├── trend.html  
            └── static/  
  

**projects 내부에 있는 crawling_code와 web_code는 api키 보안 문제로 인하여 삭제처리함**
  
## 주요 구성 요소 설명

1. **Airflow 구성 (airflow/)**  
   - **dags/**: Airflow 워크플로우 정의  
     - `crawling_naver.py`: 네이버 데이터 수집 DAG  
     - `crawling_part_1.py`: 홈쇼핑 크롤링 데이터 수집 DAG  
     - `crawling_part_2.py`: 홈쇼핑 크롤링 데이터 수집 DAG  
     - `git_pull.py`: 코드 동기화를 위한 Git Pull DAG  

2. **크롤링 스크립트 (projects/crawling/)**  
   - 각 스크립트는 특정 플랫폼에서 데이터를 수집하도록 설계됨  
   - **지원 플랫폼**:  
     - GS홈쇼핑 (라이브/TV)  
     - NS홈쇼핑 (Plus/TV)  
     - CJ온스타일 (Plus/TV)  
     - 공영홈쇼핑  
     - 현대홈쇼핑 (Plus/TV)  
     - KT, 롯데홈쇼핑, 네이버, SK스토아, SSG, W홈쇼핑 등  

3. **웹 애플리케이션 (projects/last_pj_web/)**  
   - `main.py`: Fastapi를 이용한 웹 애플리케이션 서버  
   - **templates/**: 사용자 인터페이스를 정의하는 HTML 템플릿  
     - 주요 기능:  
       - 로그인 및 회원가입  
       - 데이터 조회 및 분석  
       - 즐겨찾기 관리  
       - 검색 기능  

4. **Docker 구성**  
   - `docker-compose.yaml`: Airflow 및 웹 애플리케이션을 포함한 모든 서비스 정의  
   - **images/ys-airflow/**: 커스텀 Airflow 이미지 설정  
     - `Dockerfile`: Airflow 커스텀 이미지 구성 파일  
     - `build_docker.sh`: Docker 이미지 빌드 스크립트  
