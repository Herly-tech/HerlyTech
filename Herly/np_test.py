import numpy as np
import pandas

# persontype = np.dtype({
#     'names': ['name', 'chinese', 'english', 'math'],
#     'formats': ['S32', 'i', 'i', 'i']})
# print('personType', persontype)
# peoples = np.array([("Zhangfei", 66, 65, 30), ("Guanyu", 95, 85, 98),
#                     ("zhaoyun", 93, 92, 96), ("Huangzhong", 90, 88, 77),
#                     ("Dianwei", 80, 90, 90)],
#                    dtype=persontype)
# print('array', peoples)
# names = peoples[:]['name']
# print('names ', names)
# chineses = peoples[:]['chinese']
# englishs = peoples[:]['english']
# maths = peoples[:]['math']
# a = (chineses, englishs, maths)
# print('全班语文平均分：', np.mean(chineses))
# print('全班英语平均分：', np.mean(englishs))
# print('全班数学平均分：', np.mean(maths))
# print('全班最低分：', np.amin(a))
# print('全班最高分：', np.amax(a))
# print(np.var(a))
# print(np.std(a))
# print('成绩排序：', np.sum(a, axis=0))
# y2 = y.tostring()
# print(type(y2))

# class student:
#     def __init__(self, name, grade, perf):
#         self.name = names2
#         self.grade = y2
#         self.perf = x
#     print('%s 的分数是 %s :' %(names2, y2,))

# data = [[1, 2, 3], [4, 5, 6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)

#输出数组
# print(np.zeros(10)) # 单数会输出一维数组
# print(np.zeros((3, 5))) #复数会输出二维数组
#
# print(np.ones((4, 6))) # 数组内容为1
# print(np.empty((2, 3, 2))) #三维矩阵

# arr4= np.arange(10)
# arr4[5:8] = 10
# print(arr4)
#
# arr_slice = arr4[5:8].copy()
# arr_slice[:] = 15
# print(arr_slice)
# print(arr4)
# from pandas import DataFrame, Series
#
# data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
#         'year': [2016, 2017, 2018, 2019, 2018],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
#
#
# frame = DataFrame(data)
# frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame2)
# print(frame2['city']) #提取莫列
# print(frame2.year) #提取莫列
# frame2['new'] = 100 #生成新的一列
# print(frame2)
#
# frame2['cap'] = frame2.city == 'beijing' #生成判断变量是否在列表
# print(frame2)

# pop ={'beijing': {2008: 1.5, 2009: 2.8},
#       'shanghai': {2008: 2.0, 2009: 3.6}}
# frame3 = DataFrame(pop)
# print(frame3.T) #行列互换
#
# obj = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
# obj5 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0) #空值填充0
# print(obj5)  #series可以有一行为空，dataframe会报错
# obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# print(obj6.reindex(range(6), method='bfill')) #用前面的值填充

from numpy import nan as NA

# data10 = Series([1, NA, 2])
# print(data10.dropna()) #删除缺失值

# data2 = DataFrame([[1., 6.5, 3], [1, NA, NA],
#                  [NA, NA, NA]])
# data2[4] = NA
# print(data2)
# print(data2.dropna(axis=1, how='all'))
#
# data2.fillna(0)
# print(data2.fillna(0, inplace=True)) #用0填充缺失值, inplace（）直接填充到data
#
# print(data2)

#层次化索引
# data3 = Series(np.random.randn(10),
#                index=[['a', 'a', 'a', 'b', 'b',
#                        'b', 'c', 'c', 'd', 'd'],
#                       [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# print(data3.unstack()) # 转化成二维数据
# print(data3.unstack().stack()) # 二维数据转一维
# print(data3['b':'c']) #提取其中的值


import pandas as pd

from pandas import DataFrame

data = [[66, 65], [95, 85, 98], [95, 92, 96], [90, 88, 77],
        [80, 90, 90], [80, 90, 90]]

df1 = DataFrame(data, index=['zhangfei', 'quanyu', 'zhaoyun', 'huangzhong', 'dianwei', 'dianwei'],
                columns=['yuwen', 'yingyu', 'shuxue'])
# print(df1)

df3 = df1.fillna(0)  # 把Nan转化为0
# print(df3)
#
df3 = df3.drop_duplicates()
# print("======去重=====")
# print(df3)

#
def plus(df, n):
    df['total'] = (df[u'yuwen'] + df[u'yingyu'] + df[u'shuxue']) * n
    # df['单科合计'] = (df[u'zhangfei'] + df[u'guanyu'] + df[u'zhaoyun'] + df[u'huangzhong'] + df[u'dianwei']) * m
    return df
#
#

# df3 = df3.apply(plus, axis=1, args=(1,))
# print("====== 增加总分")
# print(df3)
#
#
def plus2(df):
    df = df.copy()
    print('hahahahahah')
    print(df)
    # df['单科合计'] = (df[u'zhangfei'] + df[u'quanyu'] + df[u'zhaoyun'] + df[u'huangzhong'] + df[u'dianwei'])
    df['min'] = df.sum()
    return df
#
#
# lamada 表达式：x 是入参，x.sum() 是返回值
f = lambda x: x.sum()
# axis = 0 时 apply 执行的时候按照上写执行
result = df3.apply(f, axis=0)

# print(result)
# df3[index['sum']] = result
# df3.append([{'sum', result}])
herly = df3.append(result, ignore_index=True)
print(herly)



