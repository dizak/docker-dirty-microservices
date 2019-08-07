FROM python:3.6

COPY ./ask.py /code/ask.py

RUN pip install flask requests

WORKDIR /code

CMD gunicorn --access-logfile - --bind 0.0.0.0:5001 ask:app
