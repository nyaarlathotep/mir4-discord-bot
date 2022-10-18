FROM python:3.8.2-slim-buster
LABEL maintainer="nyaarlathotep <raitotomoshimasu@gmail.com>"

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --fix-missing --no-install-recommends 

WORKDIR /mir4_bot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python app/main.py