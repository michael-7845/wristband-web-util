# -*- coding: utf-8 -*-  
import urllib2
import login
import json
from myConfig import server_info, login_info, notChecked
from httpreq_cookie import http_post_using_cookie

def http_post(request):
    opener = urllib2.build_opener()
    rsps = opener.open(request)
    return rsps.read()

# for web interface, deserted
def http_post_with_sid(request, session_id):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', 'JSESSIONID='+session_id))
    rsps = opener.open(request)
    return rsps.read()

# for app interface
def http_post_with_token(request, token):
    req = request + "&token=%s" % token
#    print r"* request: ", request
    req.encode("ascii")
#    print
    return http_post(req)

def build_server():
    return r"http://%s:%s" % (server_info["address"], server_info["port"])

def build_parameter(params):
    p = ""
    for (k,v) in params.items():
        p = p + "%s=%s&" % (k, v)
    if len(p) == 0:
        return p
    if p[-1] == "&":
        p = p[:-1]
    return p

def build_request(server, url, parameter):
    return r"%s%s%s" % (server, url, parameter)
    
class HttpRequest(object):
    '''
    base class for http request
    '''

    def __init__(self, url, param, response=None, checkResp=False):
        '''
        Constructor
        '''
        self.server = build_server()
        self.url = url
        self.param = param
        self.response = response
        self.checkResp = checkResp
        
    def request(self):
        r = build_request(self.server, self.url, build_parameter(self.param))
        self.rsps = http_post(r) #实际响应self.rsps
        return self.rsps
    
    def request_with_token(self, tk):
        r = build_request(self.server, self.url, build_parameter(self.param))
        self.rsps = http_post_with_token(r, tk) #实际响应self.rsps
        return self.rsps
    
    def request_with_sid(self, tk):
        r = build_request(self.server, self.url, build_parameter(self.param))
        self.rsps = http_post_with_sid(r, tk)
        return self.rsps
    
    def request_with_cookie(self):
        r = build_request(self.server, self.url, build_parameter(self.param))
        self.rsps = http_post_using_cookie(r) #实际响应self.rsps
        return self.rsps
    
    not_checked = notChecked
    
    def check_response(self):
        if self.checkResp:
            real = json.loads(self.rsps)
            expected = json.loads(self.response)
            if (type(expected[u'R']) == type(dict())):
                for skip in HttpRequest.not_checked:
                    if expected[u'R'].has_key(skip):
                        real[u'R'].pop(skip)
                        expected[u'R'].pop(skip)
            if (cmp(real, expected)==0):
                return True
            else:
                return False
        return None
                   
    
    def show(self):
        print "server: %s, url: %s, param: %s" % (self.server, self.url, self.param)
        print "request: %s" % build_request(self.server, self.url, build_parameter(self.param))
        print "expected response: %s" % (self.response)
        print
#        if self.response:
#            print json.loads(self.response)
    
def debug():
#    rsps = http_post('http://10.168.0.51:9120/usr/login1.do?email=111111@qq.com&pwd=222222')
#    print rsps
#    print build_server()
#    print build_parameter(login_info)
#    print build_request(build_server(), r"/usr/login1.do?", build_parameter(login_info))
    r = HttpRequest(r"/usr/login1.do?", login_info)
    print r.request()
    
def debug2():
    response = http_post(r'http://wristbandserver.hikemobile.com:8080/usr/login1.do?email=123@dd.com&pwd=123123')
    print response
    tk = login.parse_token(response)
    print tk.encode("ascii")
    print http_post_with_token(r"http://wristbandserver.hikemobile.com:8080/usr/updateBirth.do?birthTime=694108800000", tk)

if __name__ == '__main__':
    debug2()
    
