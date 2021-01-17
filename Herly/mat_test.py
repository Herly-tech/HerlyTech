import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings

# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

# #一条曲线
# x = np.linspace(-np.pi, np.pi, 100) #x轴的定义域为-3.14到3.14， 中间间隔100个元素
# plt.plot(x, np.sin(x))
# plt.show()  #显示所画的图

# # 多条曲线
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # 定义域为:-2pi到 2pi
# plt.figure(4, dpi=50)  # 创建图表1 , pdi=精度
# for i in range(1, 5):  # 画四条线
#     plt.plot(x, np.sin(x / i))
# plt.show()

# #直方图
# plt.figure(1, dpi=80) #创建图表1 (1是图表的名称)
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# plt.hist(data) #只要传入数据,直方图就会统计数据出现的次数
# plt.show()

# # 散点图
# x = np.arange(1, 10, 1)
# y = x*2^5
# fig = plt.figure()
# plt.scatter(x, y, c='r', marker='o') # 'r'表示散点的颜色为红色, marker表示指定三点多形状为圆形
# plt.show()

iris = pd.read_excel(r'C:\Users\15821\Desktop\test.xlsx')
# data = iris.head()
# print(data)
#
#
# #绘制散点图
# data.plot(kind='scatter', x="序号", y="鲁班")
# plt.show()

# #设置样式
# sns.set(style="white", color_codes=True)
# #设置绘制格式为散点图
# sns.jointplot(x="序号", y="鲁班", data=iris, size=5)
# #distplot绘制曲线
# sns.distplot(iris['序号'])
# plt.show()


warnings.filterwarnings("ignore")
sns.set(style="white", color_codes=True)

#FacetGrid一般绘画函数
#hue 彩色显示分类0/1/2
#plt.scatter绘制散点图
#add_legend()显示分类的描述信息
sns.FacetGrid(iris, hue="火舞", size=5).map(plt.scatter, "序号", "张飞").add_legend()

sns.FacetGrid(iris, hue="火舞", size=5).map(plt.scatter, "典韦", "安其拉").add_legend() #显示不同列
plt.show()



