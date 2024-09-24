FROM python:3.11-alpine

COPY . /server
WORKDIR /server

RUN pip install -r requirements.txt

ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]
