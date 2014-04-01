mobilmoney_sms
==============

Symple python connector for sms servise mobilmonyey telecom.

How to Use
==========

Get sms object
------------

To get sms instance object use MobilMoneySms class from client module. ::
   from mobilmoney.client import MobilMoneySms
   sms = MobilMoneySms('+79151232341', u'Message string')

MobilMoneySms need two parameters:
   1. Phone number which you want to send sms
   2. Sms message 

client = MobilMoneySmsClient('username', 'password', 'name')
client.register_sms(sms)
client.send_sms()
print(client.answer)
