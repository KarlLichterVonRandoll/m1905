## HTTPServer

* 参考代码：HTTPServer

### 功能 ： 

* httpserver 部分
> 获取 http 请求   
> 解析 http 请求  
> 将请求发送给 WebFrame  
> 从 WebFrame 接收反馈数据  
> 将数据组织为 Response 格式发送给客户端

* WebFrame 部分
> 从 httpserver 接收具体请求  
> 根据请求进行逻辑处理和数据处理  
> 将需要的数据反馈给 httpserver  

* 特点 
> 采用 httpserver 和应用处理分离的模式,降低了耦合度  
> 采用了用户配置文件的思路  
> webframe 部分采用了模拟后端框架的处理方法  

* 技术点
> httpserver 部分需要与两端建立通信  
> webFrame 部分采用多路复用接收并发请求  
> 数据传递使用 json 格式  


* 项目结构： 
``` 
         |--httpserver --HttpServer.py (主程序)      
         |             --config (httpserver配置)   
project--|
         |
         |
         |--WebFrame   --WebFrame.py (主程序代码)
                       --static （存放静态网页）
                       --views.py （ 应用处理程序） 
                       --urls.py （存放路由）
                       --settings （框架配置）
```

>交互数据格式协议

```
httpserver--> webframe  {method:'GET',info:'/'}

webframe--> httpserver {status:'200',data:'ccccc'}
```

### cookie
```
JSON --> javascript

import json

json.dumps(dict)  # 将字典转为字典格式的字符串
json.loads(js)  # 将json格式转换为字典
``` 