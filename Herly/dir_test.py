import os
print(os.path.abspath('..'))#上一级的目录对应的绝对路径  '.'现在所在的文件夹
print(os.path.exists('/Users')) #判断是否存在
print(os.path.isdir('/Users')) #判断文件或目录的性质
print(os.path.isfile('/Users'))
os.path.join('/helipolly/Backup/', 'Msg/config')