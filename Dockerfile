FROM python:3.11.3-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /usr/share/fonts/truetype/
COPY ./Impact.ttf /usr/share/fonts/truetype/Impact.ttf

CMD hypercorn -b 0.0.0.0:80 web:app