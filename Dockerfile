FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install ca-certificates -y
RUN apt-get install -y software-properties-common
RUN apt-get update --fix-missing
RUN apt-get -y install python3-pip --fix-missing

COPY ./requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY ./src .
COPY ./data ./data

EXPOSE 9200

CMD [ "python3", "./app.py" ]
