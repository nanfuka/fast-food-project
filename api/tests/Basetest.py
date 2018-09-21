from unittest import TestCase
from flask import json
from app import app
from api.model.User import User
import unittest
####################################################################################
#
#       The Base Case class comtains all the functions that need to be run in 
#       every API request and inherited by all API end point classes
#
####################################################################################


class BaseTest(TestCase):

    # Setup Client and Context for test
    def setUp(self):
        self.app = app
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()
  
    # Release Context
    def tearDown(self):
        self.context.pop()

    # Create token from login for testing pourposes
    def get_auth_token(self):
        response = self.client.post('/api/v1/login',content_type='application/json', data=json.dumps(dict(username='Deb', password='boosiko')))
        reply = json.loads(response.data.decode())
        self.assertEquals(reply['success'],True)
        if reply['success']:
            return reply['token']
        else:
            return None

    # Get Request Id for Test Pourposes
    def get_request_id(self):
        head={'Authorization':self.get_auth_token(),'content_type':'application/json'}
        
        request={'foodorder':'bacon', 'description':'fresh', 'quantity':'3'}
        response = self.client.post('/api/v1/orders',headers=head,data=json.dumps(request))
        reply = json.loads(response.data.decode())
        assert "200 OK" ==response.status
        if reply['success']:
            return reply['data']['id']

