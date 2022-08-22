from binance.websocket.spot.websocket_client import SpotWebsocketClient
import grpc
import requests
from os import getenv
from datetime import datetime

from pb import db_pb2_grpc
from pb import db_pb2

class Listener:
    ws_client = SpotWebsocketClient()
    url = getenv('BINANCE_URL')
    header = {'X-MBX-APIKEY': getenv('BINANCE_API_KEY')}
    channel = grpc.insecure_channel(getenv('DB_API'))
    ordersStub = db_pb2_grpc.OrdersStub(channel)
    walletStub = db_pb2_grpc.WalletStub(channel)

    def new_listen_key(self):
        self.listen_key = requests.post(self.url, headers=self.header).json()['listenKey']

    def renew_listen_key(self):
        requests.put(self.url, params={'listenKey': self.listen_key}, headers=self.header).json()

    def event_handler(self, event):
        if len(event) == 2:
            print(event, flush=True)
        else:
            if event['e'] == 'outboundAccountPosition':
                for i in event['B']:
                    self.walletStub.Update(db_pb2.WalletRequest(
                        exchange='binance',
                        coin=i['a'],
                        qty=i['f']
                        ))
            if event['e'] == 'executionReport':
                self.ordersStub.Update(db_pb2.OrderRequest(
                    exchange='binance',
                    symbol=event['s'],
                    order_id=event['i'],
                    price=float(event['p']),
                    qty=float(event['q']),
                    status=event['x'],
                    side=event['s'],
                    time=event['O']
                    ))

    def create_connection(self):
        self.new_listen_key()
        start_time = [int(datetime.now().strftime(
            '%-d')), int(datetime.now().strftime('%-H')), int(datetime.now().strftime('%M'))]
        self.ws_client.start()
        self.ws_client.instant_subscribe(
            stream=self.listen_key,
            callback=self.event_handler,
        )

        return start_time