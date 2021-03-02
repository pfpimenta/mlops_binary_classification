FROM ubuntu:20.04

RUN apt-get -y install python3-pip

COPY ./requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY ./src .

EXPOSE 9200

CMD [ "python3", "./app.py" ]
