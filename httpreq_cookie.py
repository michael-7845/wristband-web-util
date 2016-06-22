# -*- coding: utf-8 -*-  
import urllib2
import urllib
import cookielib

#为cookie jar 创建实例
cJar = cookielib.LWPCookieJar()
#创建HTTPCookieProcessor的opener对象
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cJar))
#安装HTTPCookieProcessor的opener
urllib2.install_opener(opener)

def http_post_using_cookie(request):
    r = urllib2.Request(request)
    h = urllib2.urlopen(r)
    return h.read()

def new_post(url,values):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
#    print "value:", values
    data = urllib.urlencode(values)
#    print "data:", data
    req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.code
    the_page = response.read()
#    print "reponse:", the_page
    return the_page

if __name__ == '__main__':
    # http_post_using_cookie()
    print http_post_using_cookie(r'http://hicamoauth.hikemobile.com/usr/login1.do?email=321321@qq.com&pwd=321321')
    print http_post_using_cookie(r'http://hicamoauth.hikemobile.com/usr/updateBirth.do?birthTime=1259510400000')
    print http_post_using_cookie(r'http://hicamoauth.hikemobile.com/activity/findActivityMonthData.do?time=1230739200000')
    # new_post()
#    print new_post(r'http://hicamoauth.hikemobile.com/usr/login1.do?email=321321@qq.com&pwd=321321')
#    print new_post(r'http://hicamoauth.hikemobile.com/usr/updateBirth.do?birthTime=1259510400000')
    