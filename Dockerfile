FROM python:3.11.2-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ['uwsgi' '--http' ':8000' '--wsgi-file' 'uwsgi.py' '--callable' 'app' '--master' '--processes' '4'' --threads' '2']