FROM python:3.6

COPY pydocs/ /flask-pydocs/pydocs/
COPY requirements.txt /flask-pydocs/requirements.txt

WORKDIR /flask-pydocs/

RUN pip install -r requirements.txt &&\
    pip install gunicorn

WORKDIR pydocs/

CMD gunicorn --access-logfile - --bind 0.0.0.0:5000 app:app 
