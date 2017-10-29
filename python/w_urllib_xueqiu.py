import urllib
import urllib.request as wurl
from bs4 import BeautifulSoup
import re
import http.cookiejar

url='https://xueqiu.com/ask/square'
# url='http://homestead'
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
header={
    'User-Agent':user_agent,
    'Referer':url,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #"Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded"}
request = wurl.Request(url,headers=header)

try:
    response = wurl.urlopen(request)
    html = response.read().decode('utf-8')
    print(html)

except urllib.error.HTTPError as e:
    print(e)
