FROM python:3.9-alpine3.15

COPY . .
WORKDIR .
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
