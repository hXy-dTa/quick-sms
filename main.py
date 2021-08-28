import requests



class SMS:

    def __init__(self, key=None):
        self.BASE_URL = 'https://api.transmitsms.com/'
        self.BASE_PATHS = {
            'send': 'send-sms.json',
            'add_contact': 'add-contacts-bulk.json',
            'check_status': 'get-sms-responses.json'
        }
        self.key = key


    def send(self, contact=None):
        if self.key:
            return {
            'status': 'success',
            'message': f'SMS Sent {self.key}'
            }
        return {
            'status': 'error',
            'message': 'API Key has not been set.\nSet it here: https://burst.transmitsms.com/profile'
            }

sms = SMS('key')
sms.send()