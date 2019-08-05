FROM python:3.6

COPY pydocs/ /flask-pydocs/pydocs/
COPY requirements.txt /flask-pydocs/requirements.txt

WORKDIR /flask-pydocs

RUN pip install -r requirements.txt

CMD python pydocs/app.py
