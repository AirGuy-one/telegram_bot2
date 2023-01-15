FROM python:3.9-alpine3.15

COPY . .
WORKDIR .
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]