FROM apache/airflow:2.6.3

USER root

RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y install wget
RUN apt-get -y install unzip
RUN apt-get -y install gnupg
RUN apt-get -y install xvfb

RUN apt-get update && apt-get -y install \
    git wget unzip gnupg xvfb fonts-liberation \
    libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libcups2 \
    libdbus-1-3 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 \
    libnss3 libxss1 lsb-release tzdata bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget -q -O /tmp/chrome-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/linux64/chrome-linux64.zip
RUN unzip /tmp/chrome-linux64.zip -d /opt/airflow
RUN rm /tmp/chrome-linux64.zip
RUN ln -s /opt/airflow/chrome /usr/bin/google-chrome

RUN wget -q -O /tmp/chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/linux64/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver-linux64.zip -d /opt/airflow
RUN rm /tmp/chromedriver-linux64.zip
RUN ln -s /opt/airflow/chromedriver /usr/bin/chromedriver

RUN mkdir -p /tmp/.X11-unix /opt/airflow/.cache/mesa_shader_cache && \
    chmod 1777 /tmp/.X11-unix && \
    chmod -R 700 /opt/airflow/.cache

ENV PATH="/opt/airflow/chrome-linux64:/opt/airflow/chromedriver-linux64:/usr/local/bin:${PATH}"

USER airflow
RUN pip install pandas
RUN pip install numpy
RUN pip install openai
RUN pip install webdriver_manager
RUN pip install selenium
RUN pip install pymongo
RUN pip install xlrd
RUN pip install pyvirtualdisplay
RUN pip install bs4
