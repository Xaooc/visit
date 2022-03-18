#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from requests import get, put, post

API_URL = 'https://ror-support.chat2desk.com/v1/%s'
API_HEADERS = {'Authorization': c2d.token, 'Content-Type': 'application/json'}
CH_ID =
MSG = 'Ой-ой! Вы позвонили в Таксопарк ГРАНД, но мы не успели поднять трубку. Вы можете задать ваш вопрос здесь.'

class Handler:

     def manually_handler(self, input_data, c2d):
         print('code: '+input_data['disconnect_reason'])
         print('phone '+input_data['from']['number'])
         if input_data['disconnect_reason']==1111:
             resp_post = post(API_URL % '/clients?phone=%s&transport=whatsapp&channel_id=%s' % (input_data['from']['number'], CH_ID),
                              headers=API_HEADERS)
             c2d.send_message(resp_post['data']['id'], MSG, to_client, CH_ID)
         return ''
