# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh


WORKDIR /app/mentalyc-backend-flask

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
ENTRYPOINT ["/entrypoint.sh"]
