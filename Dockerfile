FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install deepsmiles

WORKDIR /repo
COPY . /repo
