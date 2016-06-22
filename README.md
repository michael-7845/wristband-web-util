writeband-web-util 

web client test tool of writeband for hike

*****

# 做数据

## 设置

使用编辑工具打开myConfig.py

### 检查环境和账号信息是否正确
检查server_info和login_info部分

* 测试环境信息
> server_info = {"address": "wristbandserver.hikemobile.com", "port":"8080"}

* 测试使用账号和密码信息
> login_info = {"email":"123@dd.com", "pwd":"123123"}

### 按照myConfig.py中的说明填写你想添加的数据

修改scenarios_info部分

> 准备做数据的http请求  
> 格式 [{"url":<请求的url1>, "param":{<参数1>:<值1>, <参数2>:<值2>}, ...},   
> {"url":<请求的url2>, "param":{<参数1>:<值1>, <参数2>:<值2>}, ...},  
>  ...]  
> scenarios_info = [  
>     # request 1  
>     {"url":r"/usr/setAccountInfo.do?", #url  
>      "param":                          #请求所带参数  
>      {"nickname":"chenlong",  
>      "sex":"M",  
>      "stature":"178",  
>      "weight":"60",  
>      "birthTime":"123456789"}},   
>     # request 2  
>     {"url":r"/usr/updateBirth.do?",  
>      "param":  
>      {"birthTime":"694108800000"}},  
>     # request 3  
>     {"url":r"/usr/updateAccountInfo.do?",  
>      "param":  
>      {"fieldName":"nickname","fieldValue":"chenlong"}}  
>     ]  

## 运行

> D:\tatool\wristband>runif.py -s  
> login response: {"S":"OK","R":{"weight":60.0,"stature":178.0,"sex":"M","age":23,"email":"123@dd.com","birthTime":694108800000,"accountType":"","validateFlag":"Y","nickname":"chenlong","token":"51ed49bcdbd303fe57782f2ae04b2780"}}
> 
> request:  
> http://wristbandserver.hikemobile.com:8080/usr/setAccountInfo.do?birthTime=123456789&stature=178&nickname=chenlong&weight=60&sex=M
> http://wristbandserver.hikemobile.com:8080/usr/setAccountInfo.do?birthTime=123456789&stature=178&nickname=chenlong&weight=60&sex=M&token=51ed49bcdbd303fe57782f2ae04b2780
> 
> response: {"S":"OK","R":{"weight":60.0,"stature":178.0,"sex":"M","age":44,"email":"123@dd.com","birthTime":123456789,"accountType":"","validateFlag":"Y","nickname":"chenlong","token":"51ed49bcdbd303fe57782f2ae04b2780"}}
> 
> request:  
> http://wristbandserver.hikemobile.com:8080/usr/updateBirth.do?birthTime=694108800000
> http://wristbandserver.hikemobile.com:8080/usr/updateBirth.do?birthTime=694108800000&token=51ed49bcdbd303fe57782f2ae04b2780
> 
> ...


# 错误参数测试 

## 设置

使用编辑工具打开myConfig.py

### 检查环境和账号信息是否正确

检查server_info和login_info部分

* 测试环境信息
> server_info = {"address": "wristbandserver.hikemobile.com", "port":"8080"}

* 测试使用账号和密码信息
> login_info = {"email":"123@dd.com", "pwd":"123123"}

### 响应检查的配置
> 是否检查响应  
> 在收集数据时候, 可以设为False, 跳过响应检查点  
> isCheckRsps=True  
> 不检查的响应'R'内容的项  
> notChecked = [u'token']  

### 按照myConfig.py中的说明填写你想添加的错误参数配置

修改params_info部分

> 准备测试错误参数情形的http请求  
> 格式 [{"url":<请求的url1>, "param":{<参数1>:<值1>, <参数2>:<值2>}, "response":<url1对应的响应>, ...},   
> {"url":<请求的url2>, "param":{<参数1>:<值1>, <参数2>:<值2>}, "response":<url2对应的响应>, ...},  
> ...]  

> params_info = [  
>     # request 1  
>     {"url":r"/usr/setAccountInfo.do?", #url  
>      "param":                          #请求所带参数  
>      {"nickname":"chenlong",  
>      "sex":"M",  
>      "stature":"178",  
>      "weight":"60",  
>      "birthTime":"123456789"},  
>      "response":                        #希望的响应  
>      r'{"S":"OK","R":{"weight":60.0,"stature":178.0,"sex":"M","age":44,"email":"123@dd.com","birthTime":123456789,"accountType":"","validateFlag":"Y","nickname":"chenlong","token":"ad32d1d1a4bcb8a1bb044a254ac11cbb"}}'  
>     },  
>     # request 2  
>     {"url":r"/usr/updateBirth.do?",  
>      "param":  
>      {"birthTime":"694108800000"},  
>      "response":r'{"S":"OK","R":"23"}'  
>     },  
>     # request 3   
>     {"url":r"/usr/updateAccountInfo.do?",  
>      "param":  
>      {"fieldName":"nickname","fieldValue":"chenlong"},  
>      "response":r'{"S":"OK","R":"success"}'  
>     },  
>     ]  

## 运行

> D:\tatool\wristband>runif.py -a (执行app接口)
> or
> D:\tatool\wristband>runif.py -w (执行web接口)
> login response: {"S":"OK","R":{"weight":60.0,"stature":178.0,"sex":"M","age":23,"email":"123@dd.com","birthTime":694108800000,"accountType":"","validateFlag":"Y","nickname":"chenlong","token":"563ebe5b525d947fb15fa57e87561531"}}
> 
> request:  http://wristbandserver.hikemobile.com:8080/usr/setAccountInfo.do?birthTime=123456789&stature=178&nickname=chenlong&weight=60&sex=M  
> http://wristbandserver.hikemobile.com:8080/usr/setAccountInfo.do?birthTime=123456789&stature=178&nickname=chenlong&weight=60&sex=M&token=563ebe5b525d947fb15fa57e87561531  
>   
> response: {"S":"OK","R":{"weight":60.0,"stature":178.0,"sex":"M","age":44,"email":"123@dd.com","birthTime":123456789,"accountType":"","validateFlag":"Y","nickname":"chenlong","token":"563ebe5b525d947fb15fa57e87561531"}}  
> check result: PASS  
>   
> request:  http://wristbandserver.hikemobile.com:8080/usr/updateBirth.do?birthTime=694108800000http://wristbandserver.hikemobile.com:8080/usr/updateBirth.do?birthTime=694108800000&token=563ebe5b525d947fb15fa57e87561531  
> 
> response: {"S":"OK","R":"23"}  
> check result: PASS  
>   
> ...  


