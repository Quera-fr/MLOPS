FROM continuumio/miniconda3

WORKDIR /home/app

COPY requirements.txt /dependencies/requirements.txt

RUN pip install -r /dependencies/requirements.txt

CMD mlflow server --host 0.0.0.0 --port $PORT \
 --default-artifact-root $ARTIFACT_STORE_URI \
 --backend-store-uri $BACKEND_STORE_URI