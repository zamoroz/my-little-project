# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cwallet.proto\"?\n\rWalletRequest\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x0c\n\x04\x63oin\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\"\x1f\n\x0bReadRequest\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\".\n\x0cReadResponse\x12\x1e\n\x06wallet\x18\x01 \x03(\x0b\x32\x0e.WalletRequest\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2s\n\x06Wallet\x12\x1f\n\x04Load\x12\x0c.ReadRequest\x1a\t.Response\x12#\n\x04Read\x12\x0c.ReadRequest\x1a\r.ReadResponse\x12#\n\x06Update\x12\x0e.WalletRequest\x1a\t.Responseb\x06proto3')



_WALLETREQUEST = DESCRIPTOR.message_types_by_name['WalletRequest']
_READREQUEST = DESCRIPTOR.message_types_by_name['ReadRequest']
_READRESPONSE = DESCRIPTOR.message_types_by_name['ReadResponse']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
WalletRequest = _reflection.GeneratedProtocolMessageType('WalletRequest', (_message.Message,), {
  'DESCRIPTOR' : _WALLETREQUEST,
  '__module__' : 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:WalletRequest)
  })
_sym_db.RegisterMessage(WalletRequest)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'wallet_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

_WALLET = DESCRIPTOR.services_by_name['Wallet']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WALLETREQUEST._serialized_start=16
  _WALLETREQUEST._serialized_end=79
  _READREQUEST._serialized_start=81
  _READREQUEST._serialized_end=112
  _READRESPONSE._serialized_start=114
  _READRESPONSE._serialized_end=160
  _RESPONSE._serialized_start=162
  _RESPONSE._serialized_end=203
  _WALLET._serialized_start=205
  _WALLET._serialized_end=320
# @@protoc_insertion_point(module_scope)
