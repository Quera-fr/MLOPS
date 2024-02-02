FROM continuumio/miniconda3

WORKDIR /home/app			

RUN apt-get update			

RUN pip install boto3 pandas streamlit  

COPY . /home/app

CMD echo $Test && streamlit run --server.port $PORT Home.py