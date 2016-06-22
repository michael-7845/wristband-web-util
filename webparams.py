# -*- coding: utf-8 -*- 
import login
from myConfig import params_info, isCheckRsps
from httpreq import HttpRequest

class WebParam:
    def __init__(self):
        self.login = login.myLogin
        self.requests = []
        for s in params_info:
            if (not s.has_key("url")) \
                or (not s.has_key("param")) \
                or (not s.has_key("response")):
                continue
            r = HttpRequest(s["url"], s["param"], s["response"], isCheckRsps) 
            self.requests.append(r)
    
    def show(self):
        print self.requests
        for r in self.requests:
            r.show()
    
    def print_result(self):
        print "total requests: %d, failed requests: %d" % (self.count, self.fails)
            
    def run(self):
        print "*** Now, login ..."
        self.login.show()
        response = self.login.request_with_cookie()
        print "login response:", response
        print
        #tk = login.parse_token(response)
        
        print "*** Now, start checking ..."
        self.count = 0;
        self.fails = 0;
        for r in self.requests:
            resp = r.request_with_cookie()
            
            self.count = self.count + 1
            print "---- %d)" % (self.count)
            print r.show()
            print "real response: %s" % (resp)
            
            if r.check_response():
                print "check result: PASS" 
            else:
                self.fails = self.fails + 1
                print "check result: FAIL!!!!!!!!!!!!!!!!!!!!!!!"
            print
            
def debug():
    p = WebParam()
#    p.show()
    p.run()
    p.print_result()
    
if __name__ == '__main__':
    debug()
    