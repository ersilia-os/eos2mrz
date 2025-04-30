FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install deepsmiles==1.0.1

WORKDIR /repo
COPY . /repo
