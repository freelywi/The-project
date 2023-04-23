FROM python:3.11

RUN mkdir /SB_api_app

WORKDIR /SB_api_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src

CMD gunicorn main:app --bind 0.0.0.0:8000