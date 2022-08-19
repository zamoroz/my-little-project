from os import getenv
from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentListField,
    StringField,
    IntField,
    FloatField,
    LongField,
    ListField,
    connect,
)


connect(
    host=f"mongodb://{getenv('MONGO_CRM_HOST')}:{getenv('MONGO_CRM_PORT')}/trading_bot")

class Orders(EmbeddedDocument):
    symbol = StringField()
    order_id = StringField()
    price = FloatField()
    qty = FloatField()
    status = StringField()
    side = StringField()
    time = LongField()


class Symbols(EmbeddedDocument):
    symbol = StringField()
    base_asset = StringField()
    quote_asset = StringField()
    qty_rounder = IntField()
    price_rounder = IntField()


class Wallet(EmbeddedDocument):
    coin = StringField()
    amount = FloatField()


class Exchanges(Document):
    name = StringField()
    orders = EmbeddedDocumentListField(Orders)
    symbols = EmbeddedDocumentListField(Symbols)
    wallet = EmbeddedDocumentListField(Wallet)


class Ticker(Document):
    symbol = StringField()
    close = ListField()
    open = ListField()
    high = ListField()
    low = ListField()
    rsi = ListField()
    bol_h_200 = ListField()
    bol_l_200 = ListField()
    bol_h = ListField()
    bol_m = ListField()
    bol_l = ListField()