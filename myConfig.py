#!/usr/bin/python
# *-* coding=utf-8 *-*

# 测试环境信息
#app
#server_info = {"address": "wristbandserver.hikemobile.com", "port":"8080"} # app if.
#web
server_info = {"address": "hicamoauth.hikemobile.com","port":"80"} # web if.

# 测试使用账号和密码信息
#app
#login_info = {"email":"1234@qq.com", "pwd":"123123"}
#web
login_info = {"email":"wsr@163.com", "pwd":"321321"}

# 准备做数据的http请求
# 格式 [{"url":<请求的url1>, "param":{<参数1>:<值1>, <参数2>:<值2>}, ...}, 
#     {"url":<请求的url2>, "param":{<参数1>:<值1>, <参数2>:<值2>}, ...},
#     ...]
scenarios_info = [
    # request 1
    {"url":r"/usr/setAccountInfo.do?", #url
     "param":                          #请求所带参数
     {"nickname":"chenlong",
     "sex":"M",
     "stature":"178",
     "weight":"60",
     "birthTime":"123456789"}}, 
    # request 2
    {"url":r"/usr/updateBirth.do?",
     "param":
     {"birthTime":"694108800000"}},
    # request 3
    {"url":r"/usr/updateAccountInfo.do?",
     "param":
     {"fieldName":"nickname","fieldValue":"chenlong"}}
    ]

# 是否检查响应
# 在收集数据时候, 可以设为False, 跳过响应检查点
isCheckRsps=True
#不检查的响应'R'内容的项
notChecked = [u'token']

# 准备测试错误参数情形的http请求
# 格式 [{"url":<请求的url1>, "param":{<参数1>:<值1>, <参数2>:<值2>}, "response":<url1对应的响应>, ...}, 
#     {"url":<请求的url2>, "param":{<参数1>:<值1>, <参数2>:<值2>}, "response":<url2对应的响应>, ...},
#     ...]
params_info = [
    # request 1
    { #url
     "url":r"/usr/setAccountInfo.do?",
      #请求所带参数 
     "param":                          
     {"nickname":"chenlong",
     "sex":"M",
     "stature":"178",
     "weight":"60",
     "birthTime":"123456789"},
      #希望的响应
     "response":                        
     #r'{"S":"OK","R":{"weight":60,"age":44,"email":"1234@qq.com","stature":178,"sex":"M","birthTime":123456789,"accountType":"","validateFlag":"Y","nickname":"chenlong","token":"329a3331551b7945f3ec639e8cab9b55"}}'
     r'{"S":"OK","R":{"bmi":18.94,"weight":60,"nickname":"chenlong","validateFlag":"Y","stature":178,"sex":"M","accountType":"","age":44,"email":"wsr@163.com","headPortraitUrl":"","id":55350}}'
    },
    # request 2
    {"url":r"/usr/updateBirth.do?",
     "param":
     {"birthTime":"694108800000"},
     "response":r'{"S":"OK","R":"23"}'
    },
    # request 3
    {"url":r"/usr/updateAccountInfo.do?",
     "param":
     {"fieldName":"nickname","fieldValue":"chenlong"},
     "response":r'{"S":"OK","R":"success"}'
    },
    ]
   
def show_config():
    print server_info
    print login_info
    print scenarios_info

if __name__ == '__main__':
    show_config()