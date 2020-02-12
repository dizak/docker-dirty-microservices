from flask import Flask
from flask import jsonify
from requests import Session


def setup_connector(app, name='default', **kwargs):
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    if 'connectors' not in app.extensions:
        app.extensions['connectors'] = {}
    session = Session()
    if 'auth' in kwargs:
        session['auth'] = kwargs['auth']
    headers = kwargs.get('headers', {})
    if 'ContentType' not in headers:
        headers['ContentType'] = 'application/json'
    session.headers.update(headers)
    app.extensions['connectors'][name] = session
    return session

def get_connector(app, name='default'):
    return app.extensions['connectors'][name]


app = Flask(__name__)

setup_connector(app)

@app.route('/ask/str/<text>', methods=['GET', 'POST'])
def ask_str(text):
    with get_connector(app) as conn:
        result = conn.get(f'http://pydocs:5000/pydocs/str/{text}')
    return str(result.content)

@app.route('/ask/int/<text>', methods=['GET', 'POST'])
def ask_int(text):
    with get_connector(app) as conn:
        result = conn.get(f'http://pydocs:5000/pydocs/int/{text}')
    return str(result.content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
