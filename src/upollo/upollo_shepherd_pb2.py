# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: upollo/upollo_shepherd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from upollo import upollo_public_pb2 as upollo_dot_upollo__public__pb2
from upollo import upollo_shadow_pb2 as upollo_dot_upollo__shadow__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cupollo/upollo_shepherd.proto\x12\x07uwproto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1aupollo/upollo_public.proto\x1a\x1aupollo/upollo_shadow.proto\"u\n\x0eWebHookRequest\x12+\n\x08\x61nalysis\x18\x01 \x01(\x0b\x32\x19.uwproto.AnalysisResponse\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0c\n\x04urls\x18\x03 \x03(\t\x12\x14\n\x0cweb_hook_key\x18\x04 \x01(\t\"m\n\x0fWebHookResponse\x12+\n\x08\x61nalysis\x18\x01 \x01(\x0b\x32\x19.uwproto.AnalysisResponse\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"C\n\rDeviceRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0e\n\x06global\x18\x03 \x01(\x08\"!\n\x0e\x44\x65viceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"$\n\x11\x44\x65viceListRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\":\n\x12\x44\x65viceListResponse\x12$\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x13.uwproto.DeviceInfo\"o\n\x0bSignedToken\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\r\n\x05nonce\x18\x03 \x01(\x0c\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x81\x02\n\rVerifyRequest\x12\x13\n\x0b\x65vent_token\x18\x01 \x01(\t\x12#\n\x08userinfo\x18\x02 \x01(\x0b\x32\x11.uwproto.UserInfo\x12\x45\n\x16\x63hallenge_verification\x18\x04 \x01(\x0b\x32%.uwproto.ChallengeVerificationRequest\x12*\n\nevent_type\x18\x05 \x01(\x0e\x32\x12.uwproto.EventTypeB\x02\x18\x01\x12\'\n\x1b\x63ustomer_defined_event_type\x18\x06 \x01(\tB\x02\x18\x01\x12\x1a\n\x0esub_event_type\x18\x08 \x01(\tB\x02\x18\x01\"\xe7\x01\n\x1c\x43hallengeVerificationRequest\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\t\x12\x17\n\x0fsecret_response\x18\x02 \x01(\t\x12$\n\x1cwebauthn_credential_response\x18\x03 \x01(\x0c\x12#\n\x08userinfo\x18\x06 \x01(\x0b\x32\x11.uwproto.UserInfo\x12\x11\n\tdevice_id\x18\x07 \x01(\t\x12$\n\x04type\x18\x05 \x01(\x0e\x32\x16.uwproto.ChallengeType\x12\x14\n\x0creport_token\x18\x08 \x01(\t\"\xca\x01\n\x1d\x43hallengeVerificationResponse\x12\x44\n challenge_completed_successfully\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12&\n\nevent_type\x18\x03 \x01(\x0e\x32\x12.uwproto.EventType\x12#\n\x1b\x63ustomer_defined_event_type\x18\x04 \x01(\t\x12\x16\n\x0esub_event_type\x18\x05 \x01(\t\"\xeb\x01\n\x16\x43reateChallengeRequest\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.uwproto.ChallengeType\x12#\n\x08userinfo\x18\x02 \x01(\x0b\x32\x11.uwproto.UserInfo\x12\x11\n\tdevice_id\x18\x04 \x01(\t\x12\x0e\n\x06origin\x18\x05 \x01(\t\x12&\n\nevent_type\x18\x06 \x01(\x0e\x32\x12.uwproto.EventType\x12#\n\x1b\x63ustomer_defined_event_type\x18\x07 \x01(\t\x12\x16\n\x0esub_event_type\x18\x08 \x01(\t\"\x9f\x01\n\x17\x43reateChallengeResponse\x12\x14\n\x0c\x63hallenge_id\x18\x01 \x01(\t\x12*\n\x06\x65xpiry\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x14webauthn_credentials\x18\x03 \x01(\x0c\x12$\n\x04type\x18\x04 \x01(\x0e\x32\x16.uwproto.ChallengeType\"y\n\x11TrackEventRequest\x12#\n\x08userinfo\x18\x01 \x01(\x0b\x32\x11.uwproto.UserInfo\x12\x1d\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x0e.uwproto.Event\x12 \n\x07library\x18\x03 \x01(\x0b\x32\x0f.uwGrpc.Library\")\n\x17\x43ompanyInfoFetchRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t2\x8c\x04\n\x08Shepherd\x12>\n\x05Track\x12\x1a.uwproto.TrackEventRequest\x1a\x19.uwproto.AnalysisResponse\x12;\n\x06Verify\x12\x16.uwproto.VerifyRequest\x1a\x19.uwproto.AnalysisResponse\x12T\n\x0f\x43reateChallenge\x12\x1f.uwproto.CreateChallengeRequest\x1a .uwproto.CreateChallengeResponse\x12`\n\x0fVerifyChallenge\x12%.uwproto.ChallengeVerificationRequest\x1a&.uwproto.ChallengeVerificationResponse\x12@\n\rApproveDevice\x12\x16.uwproto.DeviceRequest\x1a\x17.uwproto.DeviceResponse\x12?\n\x0cReportDevice\x12\x16.uwproto.DeviceRequest\x1a\x17.uwproto.DeviceResponse\x12H\n\rGetDeviceList\x12\x1a.uwproto.DeviceListRequest\x1a\x1b.uwproto.DeviceListResponseBN\n\x0f\x61i.upollo.protoP\x01Z/github.com/userwatch/uw1/protos/uwprotoshepherd\xa2\x02\x07UpProtob\x06proto3')



_WEBHOOKREQUEST = DESCRIPTOR.message_types_by_name['WebHookRequest']
_WEBHOOKRESPONSE = DESCRIPTOR.message_types_by_name['WebHookResponse']
_DEVICEREQUEST = DESCRIPTOR.message_types_by_name['DeviceRequest']
_DEVICERESPONSE = DESCRIPTOR.message_types_by_name['DeviceResponse']
_DEVICELISTREQUEST = DESCRIPTOR.message_types_by_name['DeviceListRequest']
_DEVICELISTRESPONSE = DESCRIPTOR.message_types_by_name['DeviceListResponse']
_SIGNEDTOKEN = DESCRIPTOR.message_types_by_name['SignedToken']
_VERIFYREQUEST = DESCRIPTOR.message_types_by_name['VerifyRequest']
_CHALLENGEVERIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['ChallengeVerificationRequest']
_CHALLENGEVERIFICATIONRESPONSE = DESCRIPTOR.message_types_by_name['ChallengeVerificationResponse']
_CREATECHALLENGEREQUEST = DESCRIPTOR.message_types_by_name['CreateChallengeRequest']
_CREATECHALLENGERESPONSE = DESCRIPTOR.message_types_by_name['CreateChallengeResponse']
_TRACKEVENTREQUEST = DESCRIPTOR.message_types_by_name['TrackEventRequest']
_COMPANYINFOFETCHREQUEST = DESCRIPTOR.message_types_by_name['CompanyInfoFetchRequest']
WebHookRequest = _reflection.GeneratedProtocolMessageType('WebHookRequest', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOKREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.WebHookRequest)
  })
_sym_db.RegisterMessage(WebHookRequest)

WebHookResponse = _reflection.GeneratedProtocolMessageType('WebHookResponse', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOKRESPONSE,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.WebHookResponse)
  })
_sym_db.RegisterMessage(WebHookResponse)

DeviceRequest = _reflection.GeneratedProtocolMessageType('DeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.DeviceRequest)
  })
_sym_db.RegisterMessage(DeviceRequest)

DeviceResponse = _reflection.GeneratedProtocolMessageType('DeviceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEVICERESPONSE,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.DeviceResponse)
  })
_sym_db.RegisterMessage(DeviceResponse)

DeviceListRequest = _reflection.GeneratedProtocolMessageType('DeviceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEVICELISTREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.DeviceListRequest)
  })
_sym_db.RegisterMessage(DeviceListRequest)

DeviceListResponse = _reflection.GeneratedProtocolMessageType('DeviceListResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEVICELISTRESPONSE,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.DeviceListResponse)
  })
_sym_db.RegisterMessage(DeviceListResponse)

SignedToken = _reflection.GeneratedProtocolMessageType('SignedToken', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDTOKEN,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.SignedToken)
  })
_sym_db.RegisterMessage(SignedToken)

VerifyRequest = _reflection.GeneratedProtocolMessageType('VerifyRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.VerifyRequest)
  })
_sym_db.RegisterMessage(VerifyRequest)

ChallengeVerificationRequest = _reflection.GeneratedProtocolMessageType('ChallengeVerificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEVERIFICATIONREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.ChallengeVerificationRequest)
  })
_sym_db.RegisterMessage(ChallengeVerificationRequest)

ChallengeVerificationResponse = _reflection.GeneratedProtocolMessageType('ChallengeVerificationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHALLENGEVERIFICATIONRESPONSE,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.ChallengeVerificationResponse)
  })
_sym_db.RegisterMessage(ChallengeVerificationResponse)

CreateChallengeRequest = _reflection.GeneratedProtocolMessageType('CreateChallengeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECHALLENGEREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.CreateChallengeRequest)
  })
_sym_db.RegisterMessage(CreateChallengeRequest)

CreateChallengeResponse = _reflection.GeneratedProtocolMessageType('CreateChallengeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECHALLENGERESPONSE,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.CreateChallengeResponse)
  })
_sym_db.RegisterMessage(CreateChallengeResponse)

TrackEventRequest = _reflection.GeneratedProtocolMessageType('TrackEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACKEVENTREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.TrackEventRequest)
  })
_sym_db.RegisterMessage(TrackEventRequest)

CompanyInfoFetchRequest = _reflection.GeneratedProtocolMessageType('CompanyInfoFetchRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMPANYINFOFETCHREQUEST,
  '__module__' : 'upollo.upollo_shepherd_pb2'
  # @@protoc_insertion_point(class_scope:uwproto.CompanyInfoFetchRequest)
  })
_sym_db.RegisterMessage(CompanyInfoFetchRequest)

_SHEPHERD = DESCRIPTOR.services_by_name['Shepherd']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017ai.upollo.protoP\001Z/github.com/userwatch/uw1/protos/uwprotoshepherd\242\002\007UpProto'
  _VERIFYREQUEST.fields_by_name['event_type']._options = None
  _VERIFYREQUEST.fields_by_name['event_type']._serialized_options = b'\030\001'
  _VERIFYREQUEST.fields_by_name['customer_defined_event_type']._options = None
  _VERIFYREQUEST.fields_by_name['customer_defined_event_type']._serialized_options = b'\030\001'
  _VERIFYREQUEST.fields_by_name['sub_event_type']._options = None
  _VERIFYREQUEST.fields_by_name['sub_event_type']._serialized_options = b'\030\001'
  _WEBHOOKREQUEST._serialized_start=162
  _WEBHOOKREQUEST._serialized_end=279
  _WEBHOOKRESPONSE._serialized_start=281
  _WEBHOOKRESPONSE._serialized_end=390
  _DEVICEREQUEST._serialized_start=392
  _DEVICEREQUEST._serialized_end=459
  _DEVICERESPONSE._serialized_start=461
  _DEVICERESPONSE._serialized_end=494
  _DEVICELISTREQUEST._serialized_start=496
  _DEVICELISTREQUEST._serialized_end=532
  _DEVICELISTRESPONSE._serialized_start=534
  _DEVICELISTRESPONSE._serialized_end=592
  _SIGNEDTOKEN._serialized_start=594
  _SIGNEDTOKEN._serialized_end=705
  _VERIFYREQUEST._serialized_start=708
  _VERIFYREQUEST._serialized_end=965
  _CHALLENGEVERIFICATIONREQUEST._serialized_start=968
  _CHALLENGEVERIFICATIONREQUEST._serialized_end=1199
  _CHALLENGEVERIFICATIONRESPONSE._serialized_start=1202
  _CHALLENGEVERIFICATIONRESPONSE._serialized_end=1404
  _CREATECHALLENGEREQUEST._serialized_start=1407
  _CREATECHALLENGEREQUEST._serialized_end=1642
  _CREATECHALLENGERESPONSE._serialized_start=1645
  _CREATECHALLENGERESPONSE._serialized_end=1804
  _TRACKEVENTREQUEST._serialized_start=1806
  _TRACKEVENTREQUEST._serialized_end=1927
  _COMPANYINFOFETCHREQUEST._serialized_start=1929
  _COMPANYINFOFETCHREQUEST._serialized_end=1970
  _SHEPHERD._serialized_start=1973
  _SHEPHERD._serialized_end=2497
# @@protoc_insertion_point(module_scope)
