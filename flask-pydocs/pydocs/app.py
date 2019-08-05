from flask import Flask
from redis import Redis
from redis import RedisError


redis = Redis(host='redis', db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

@app.route('/pydocs/str/<text>')
def pydocs_str(text):
    try:
        visits = redis.incr('counter')
    except RedisError:
        visits = 'Could not connetc to redis'
    try:
        response = "{}\n{}\n".format(getattr(str, text).__doc__, visits)
    except AttributeError:
        response = 'Method not found\n'
    return response

@app.route('/pydocs/int/<text>', )
def pydocs_int(text):
    try:
        response = "{}\n{}\n".format(getattr(int, text).__doc__, visits)
    except AttributeError:
        response = 'Method not found\n'
    return response

if __name__ == '__main__':
    app.run("0.0.0.0")
