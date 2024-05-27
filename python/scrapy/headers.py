# -- coding: utf-8 -
"""
@project    :HandBook
@file       :headers.py
@Author     :wooght
@Date       :2024/5/23 17:19
@Content    :user-agent 列表
"""

"""
====>Request Headers:

    User-Agent: 
    Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.11082
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0
    
    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/125 Version/11.1.1 Safari/605.1.15


    Cache区域:
        Cache-Control: Public/Private/no-cache/max-age=3600
            Response-Request遵循缓存机制,以上分别表示
                    任何缓存来缓存/当前用户缓存/不缓存/存储时间(单位秒)
        If-Modified-Since   对比服务器时间
        If-None-Match       
        Pragma:no-cache     只有一个用法,及不缓存

    Client区域:   
        Accept:text/html    客户端可以接受text/html类型数据    
        Accept: */*         客户端可以接受任意数据
        Accept:application/json 客户端接受json
        Accept:text/html,*/*, application/json 可以同时声明多个
        
        Accept-Encoding:gzip,deflate,br 客户端接受的方式
        Accept-Language:zh-CN,zh-Hans;q=0.9 客户端语言
        Accept-Charset:utf-8    客户端声明字符集
        
    Cookie区域:
        发送Cookie到HTTP服务器,字典类型
        name:value
    
    Miscellaneous区域:
        Referer:http://www.baidu.com        上下文信息,告诉服务器从哪个链接来访问的
        Origin:作者,及谁发起的
    
    Entity区域:
        Content-Length: 38      发送的数据长度
        Content-Type: text/html,application/json,text/xml,image/jpeg,application/octet-stream ;charset=utf-8
        multipart/form-data 需要提交表单及表单里要上传文件等
        
    Transport区域:
        Connection: keep-alive, close
                完成后连接状态:保持连接,关闭连接
        Host:指定被请求资源的internet主机和端口号,一般是域名主要部分
                
    Security区域:
    

====>Response Headers:
    

"""