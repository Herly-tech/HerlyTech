#记录生肖，根据年份来判断
#python对双引号和单引号没有区分，当str里面含有单引号就用双引号
chinses_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

#print(Chinses_zodiac[0:4]) #从后往前用负数
#year = 2018
#print(year % 12)
#print(Chinses_zodiac[year % 12])

#print('狗'in Chinses_zodiac)
#year = int(input('请输入出生年份：'))
#for cz in Chinses_zodiac:
 #   print(cz)

#for i in range(1,13):
#    print(i)

#for year in range(2000, 2019):
 #   print('%s 年的生肖是 %s' % (year, chinses_zodiac[year % 12]


num = 5
while True:
    num = num + 1
    if num > 10:
        continue

    print(num)