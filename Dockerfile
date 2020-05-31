FROM python:3.8

# Install external libraries for Python
COPY requirements.txt .
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt && \
    rm -f requirements.txt

COPY ./src /app

WORKDIR /app

CMD ["python3", "main.py"]