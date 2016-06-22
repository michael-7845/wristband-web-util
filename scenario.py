# -*- coding: utf-8 -*-  
'''
Created on 2014-8-26

@author: Kemin Yu
'''
import login
from myConfig import scenarios_info
from httpreq import HttpRequest

class Scenario:
    def __init__(self):
        self.login = login.myLogin
        self.requests = []
        for s in scenarios_info:
            if (not s.has_key("url")) or (not s.has_key("param")):
                continue
            r = HttpRequest(s["url"], s["param"])
            self.requests.append(r)
            
    def show(self):
        print self.requests
        for r in self.requests:
            r.show()
            
    def run(self):
        response = self.login.request()
        print "login response:", response
        print
        tk = login.parse_token(response)
        for r in self.requests:
            resp = r.request_with_token(tk)
            print "response:", resp
            print r.check_response()

def debug():
    s = Scenario()
    s.show()
#    s.run()

if __name__ == '__main__':
    debug()