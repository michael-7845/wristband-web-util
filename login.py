# -*- coding: utf-8 -*-  
'''
Created on 2014-8-26

@author: Kemin Yu
'''
import json
from httpreq import HttpRequest
from myConfig import login_info

myLogin = HttpRequest(r"/usr/login1.do?", login_info)

def parse_token(response):
    resp_json = json.loads(response)
    R=resp_json['R']
    token = R[u'token']
    return token

if __name__ == '__main__':
    print myLogin.request()