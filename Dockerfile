FROM python:3.11.2
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt update && apt install uwsgi -y

COPY . .

RUN mkdir -p /usr/share/fonts/truetype/
COPY ./Impact.ttf /usr/share/fonts/truetype/Impact.ttf

CMD uwsgi --http-socket :8000 --wsgi-file uwsgi.py --callable app --master --processes 4 --threads 2