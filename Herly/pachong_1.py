from urllib import request
from urllib import parse  #处理数据


url = 'http://www.baidu.com'  #http网页协议
response = request.urlopen(url, timeout=1) # 解析路径, timeout定时，超过时间则放弃打开网页
print(response.read().decode('utf-8'))  #读取网页内容







