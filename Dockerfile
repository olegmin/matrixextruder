FROM python:3.8

COPY ./src /app

WORKDIR /app

CMD ["python3", "main.py"]