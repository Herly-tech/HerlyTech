#日常用比较广泛的模块是：
#1，文字处理的 re
#2，日期类型的time，datetime
#3，数字和数字类型的math，random
#4，文件和目录访问的pathlib，os.path
#5，数据压缩和归档的tarfile
#6，通用操作系统的os，logging，argparse
#7，多线程的threading,queue
#8，Internet数据处理的base64
#9，结构化标记处理工具的huml,xml
#10，开发工具unitest
#11，调试攻击的timeit
#12,软件包发布的venv
#13，运行服务的__main__

#主要的正则表达符号
#.(全部字符,复数个点匹配相对应的数量的字符） ^（从开头搜索） $（从后到前匹配） *(字符前面的字符出现零次或无数次） +（字符前面的字符出现一次或无数次）
# ?（出现零次或一次，其他） {m}（表示前面的字符要出现指定的次数） {m,n}（表示前面的字符要出现指定的次数或次数） [] |（或者）
# 转义符号：\d=[0,1,2,3,4,5,6,7,8,9]/[0-9] \D(匹配不包含数字的） \s=[a到z的所有字母] ()=（指定需要提取的内容）
# ^$（表示此行是空行）
# .*?（不使用贪婪模式）
# r(后面的内容原样输出）

import re

#match匹配功能-完全匹配-进行fenzu
# p = re.compile(r'(\d+)-(\d+)-(\d+)')  #正则表达式模式编译为正则表达式对象
# print(p.match('2018-05-01').group(1)) #group()函数括号里面的数字对应相应的集合）
# print(p.match('2018-05-01').groups()) #groups()函数可取出所有集合
#
#
# year, month, day = p.match('2018-05-01').groups()
# print(year)

# #search匹配功能-不完全匹配-搜索
# print(p.search('aa2018-05-01bb'))
#
# #sub替换功能  subn()返回元组
# phone = '123-456-789' #这是电话号码
# p2 = re.sub(r'#.*$', '', phone)
# print(p2)
# p3 = re.sub(r'\D', '', p2)
# print(p3)
#
# # findall() #进行匹配多次
# f1 = re.findall('a', 'This is a beautiful place') #从左到右扫描该字符串，并以找到的顺序返回匹配项
# print(f1)
#
# #fullmatch() 正则完整匹配
# fm1 = re.fullmatch('\w+', 'abced').group()
# print(fm1)
# fm2 = re.fullmatch('abdcs', 'abdcs').group() #如果不匹配否则返回false
# print(fm2)

# # re.split() 拆分字符串
# s1 = re.split('[ab]', 'abcd')
# print(s1)
# s2 = re.split(r'(\W+)', 'Words, words, words.')
# print(s2)
# s3 = re.split(r'\W+', 'Words, words, words.')
# print(s3)
# s4 = re.split(r'\W+', 'Words, words, words.', 1) #maxsplit=1 最多匹配一次
# print(s4)
# s5 = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
# print(s5)

# #finditer() 迭代器
# ret = re.finditer('[ab]', 'this is a beautiful place')
# print(ret)
# print(next(ret).group())
#
# for i in ret:
#     print(i)

import tensorflow
# 用Git Hub下载模块或代码  Gitc lone + 路径


