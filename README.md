# docker-dirty-microservices

This repo serves as an example of nearly-deploy implementation of Flask-based microservices with nginx as a reverse proxy.
Microservices are developed independently in kind of separate bubbles.
For instance, ```flask-pydocs``` has basic structure of a proper Python package.
```flask-ask``` on the other hand, is ugly.

Building images:

1. ```docker build -t nginx:0.0.1 .

1. ```docker build -t flask-ask:0.0.0 .

1. ```docker build -t pydocs:0.0.0 .

Running services:

```docker-compose up```

This is not a stack! No swarm here!


