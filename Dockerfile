FROM apache/airflow:2.10.4

ADD requirements.txt .
#RUN pip install -r requirements.txt
RUN python -m venv venv
RUN pip install -r requirements.txt