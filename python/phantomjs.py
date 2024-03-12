# -*- coding: UTF-8 -*-
from selenium import webdriver

#headers 内容
cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = True
cap["phantomjs.page.settings.disk-cache"] = True
cap["phantomjs.page.customHeaders.Cookie"] = 'SINAGLOBAL=3955422793326.2764.1451802953297; '
cap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

#创建PhantomJS实例 service_args功能是能访问https phantomjs没有加入path目录则要在运行中加入绝对地址 在windows中,要放在python的安装目录下 D:\Python34\Scripts\phantomjs.exe
#driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'],executable_path="F:\homestead/phantomjs",desired_capabilities=cap)
driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'],desired_capabilities=cap)
# driver = webdriver.Chrome()
url = ['http://homestead','https://xueqiu.com/','http://www.baidu.com']
driver.get(url[1])
data = driver.page_source                           #得到所有html代码
#data = driver.title                                #得到网页标题

file = open('phantomjs.json','w',encoding='utf-8')
file.write(data)
try:
    print(data)
except:
    print('error')

driver.quit()                                       #关闭phantomjs对象
