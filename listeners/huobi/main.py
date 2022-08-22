import websocket
import json
import ssl
from datetime import datetime
from urllib import parse
import hmac
from hashlib import sha256
import base64
import json
from os import getenv

from .api_client import Client

HOST = getenv('HOST')
PATH = getenv('PATH')
ACCESS_KEY = getenv('ACCESS_KEY')
SECRET_KEY = getenv('SECRET_KEY')

def get_params(method: str, host: str, path: str, access_key: str, secret_key: str, params: dict = None):
    if params is None:
        params = {}
    params['accessKey'] = access_key
    params['signatureVersion'] = '2.1'
    params['signatureMethod'] = 'HmacSHA256'

    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params['timestamp'] = timestamp

    suffix = ''
    for k in sorted(params.keys()):
        suffix += '&{}={}'.format(k, parse.quote(params[k], safe=''))
    if suffix != '':
        suffix = suffix[1:]
    payload = '{}\n{}\n{}\n{}'.format(method.upper(), host, path, suffix)

    digest = hmac.new(secret_key.encode('utf8'), payload.encode(
        'utf8'), digestmod=sha256).digest()
    signature = base64.b64encode(digest).decode()
    params['signature'] = signature
    params['authType'] = 'api'
    return params

def on_message(connection, message):
    client = Client()
    data = json.loads(message)
    if data['action'] == 'req':
        if data['code'] == 200:
            print('INFO:    ', 'Signed up')
            for i in client.get_symbols():
                connection.send('{"action": "sub", "ch": "orders#' + i + '"}')
            connection.send('{"action": "sub", "ch": "accounts.update#1"}')
    if data['action'] == 'ping':
        payload = {
            'action': 'pong',
            'data': {
                'ts': data['data']['ts']
            }
        }
        connection.send(json.dumps(payload))
    if data['action'] == 'push':
        if 'order' in data['ch'] and len(data['data']) != 0:
            if data['data']['eventType'] == 'trigger':
                on_error(connection, data['data']['errMessage'])
            else: client.order_handler(data['data'])
        elif 'accounts' in data['ch'] and len(data['data']) != 0:
            client.wallet_handler(data['data'])
        print('INFO:    ', data['data'])
    return

def on_error(connection, error):
    print('error',error)

def on_close(connection):
    print('Connection was closed')

def on_open(connection):
    print('INFO:    ', 'Connected')
    params = get_params('GET', HOST, PATH, ACCESS_KEY, SECRET_KEY)
    payload = params.copy()
    payload['authType'] = 'api'
    payload['action'] = 'req'
    payload['ch'] = 'auth'
    payload['params'] = params
    connection.send(json.dumps(payload))

socket = websocket.WebSocketApp(f"wss://{HOST}{PATH}",
                                on_message=on_message,
                                on_close=on_close,
                                on_open=on_open,
                                on_error=on_error
                                )

if __name__ == '__main__':
    socket.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
