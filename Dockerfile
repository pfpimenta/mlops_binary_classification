FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install ca-certificates -y
RUN apt-get install -y software-properties-common
RUN apt-get update --fix-missing
RUN apt-get -y install python3-pip unzip --fix-missing

# install dependencies
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY ./src .

# get data from kaggle
ENV KAGGLE_USERNAME=pfpimenta
ENV KAGGLE_KEY=ac1e201e841350b4a90fb0debf8b4dc1
RUN kaggle datasets download -d mlg-ulb/creditcardfraud -p ./data
RUN unzip ./data/creditcardfraud.zip -d ./data
RUN rm ./data/creditcardfraud.zip

EXPOSE 9200

CMD [ "python3", "./app.py" ]
