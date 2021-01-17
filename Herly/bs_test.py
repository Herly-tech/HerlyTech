from bs4 import BeautifulSoup
import requests
from functools import reduce

html = requests.get('https://www.qiushibaike.com/text/')
soup = BeautifulSoup(html.content, 'lxml')
# 根据标签查找
contents = soup.find_all('div', class_='content')
# for content in contents:
#     print(content.span.getText())
#     print('==========')

# 根据 selector 查找元素
links = soup.select('div > a > div > span')


# for link in links:
#     print(link.getText())


def str2int(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    strs = ''
    for char in iter(s):
        if char in DIGITS:
            strs = strs + char

    if len(strs):
        return 0
    return float(strs)


def fetchWeatherInfo():
    weather = requests.get('http://www.weather.com.cn/weather/101020100.shtml')
    weatherSoup = BeautifulSoup(weather.content, 'lxml')

    temps = weatherSoup.select('div > ul > li.sky.skyid.lv2.on > p.tem > i')
    for temp in temps:
        floatTemp = str2int(temp.getText())
        if floatTemp > 25:
            print('今天天气', temp.getText(), 'a little hot')
        else:
            print('today is ', temp.getText(), 'a little cold')


fetchWeatherInfo()


def fetchShit():
    print('Hello, are you herly')
