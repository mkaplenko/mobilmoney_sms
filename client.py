# -*- coding: utf-8 -*-
__author__ = 'mkaplenko'
import httplib
import time


class MobilMoneySms(object):
    def __init__(self, phone_to, message):
        self.phone_to = phone_to
        self.message = message
        self.sync = int(time.time()*100)


class MobilMoneySmsClient(object):
    connection_host = 'gate.mobilmoney.ru'
    response = None
    sms = None
    sync = 1

    def __init__(self, login, password, originator):
        self.login = login
        self.password = password
        self.originator = originator

    def register_sms(self, sms_instance):
        self.sms = sms_instance

    def request_body(self):
        data_kwargs = {
            'login': self.login,
            'password': self.password,
            'originator': self.originator,
            'phone_to': self.sms.phone_to,
            'message': self.sms.message,
            'sync': unicode(self.sms.sync)
        }
        data = u'''
        <?xml version="1.0" encoding="utf-8"?>
        <request method="SendSMSFull">
             <login>{login}</login>
             <pwd>{password}</pwd>
             <originator>{originator}</originator>
             <phone_to>{phone_to}</phone_to>
             <message>{message}</message>
             <sync>{sync}</sync>
        </request>

        '''.format(**data_kwargs).encode('utf-8')

        return data

    def send_sms(self):
        connection = httplib.HTTPConnection(self.connection_host)
        connection.request('POST', '/', self.request_body())
        self.response = connection.getresponse()

    @property
    def answer(self):
        return self.response.read() if self.response else None

if __name__ == '__main__':
    sms = MobilMoneySms('+79151234567', u'Привет мир! Я тестирую смс!')
    client = MobilMoneySmsClient('my_login', 'my_password', 'my_originator_name')
    client.register_sms(sms)
    client.send_sms()
    print(client.answer)
