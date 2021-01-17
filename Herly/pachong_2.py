from urllib import request
from urllib import parse  #处理数据
#
# data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')

# response = request.urlopen('http://www.baidu.com/get', data=data)
# print(response.read().decode('utf-8'))
#
#
response1 = request.urlopen('http://www.baidu.com/post', timeout=1)
print(response1.read().decode('utf-8'))

# response2 = request.urlopen('http://www.baidu.com/post', timeout=0.01)
# print(response2.read().decode('utf-8'))

import urllib
import socket

try:
    response2 = urllib.request.urlopen('http://www.baidu.com/post', timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


