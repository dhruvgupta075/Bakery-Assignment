FROM ubuntu:20.04


WORKDIR /app

COPY requirements.txt requirements.txt 

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py","runserver","0.0.0.0:8080" ]