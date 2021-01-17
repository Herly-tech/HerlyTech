# print('abc', end='\n\n')
# print('abc')

# def func(a, b, c):
#     print('a=%s' %a)
#     print('b=%s' %b)
#     print('c=%s' %c)
#
#
# func(1, c=3, b=2)

# # 取得参数的个数（函数可变长参数）
# def howlong(first, *other):
#     print(1 + len(other))
#     return
#
# howlong(123)

# #函数变量作用域
# var1 = 123
#
#
# def func():
#     global var1
#     var1 = 456
#     print(var1)
#
#
# func()
# print(var1)

# #d迭代器
# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# for i in range(10, 20, 0.5):
#     print(i)

# #生成器
# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
# for i in frange(10, 20, 0.5):
#     print(i)
#
# #lambba表达式
# def add(x, y):return x+y
# lambda x,y:x+y
#
# filter函数
# print(add(3, 5))
# a = [1, 2, 3, 4, 5, 6,7]
# print(list(filter(lambda x:x>2, a))

# #求和/reduce函数
# from functools import reduce
# print(reduce(lambda x, y: x+y, range(1, 100)))
# #zip函数
# zip(1, 2, 3),(4, 5, 6)
# for i in zip(1, 2, 3),(4, 5,6):
#     print(i)

# #装饰器
# # sleep方法
# import time
# print(time.time) #从1970,1,1到现在的时间
# time.sleep(3)
#
# #timmer函数
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("运行时间是 %s 秒：" %(stop_time - start_time))
#     return wrapper
#
# @timmer
# def i_can_sleep():
#     time.sleep(3)
#
# print(i_can_sleep())

# # 装饰器使用
#
#
# def new_tips(argv):
#     def tips(func):
#         def nei(a, b):
#             print('start %s %s' % (argv, func.__name__))
#             func(a, b)
#             print('stop')
#
#         return nei
#
#     return tips
#
#
# @new_tips('add_module')
# def add(a, b):
#     print(a + b)
#
#
# @new_tips('sub_module')
# def sub(a, b):
#     print(a - b)
#
#
# print(add(4, 5))
# print(sub(5, 5))

# 上下文管理器
fd = open('name.txt')
try:
    for line in fd:
        print(line)
finally:
    fd.close()

#可简化为
with open('name.txt') as f:
    for line in f:
        print(line)

# 笔记：匿名函数lambda（）

# # 引入模块
# import os
# import numpy as np
# from time import sleep

