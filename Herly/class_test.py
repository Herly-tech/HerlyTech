# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s ,hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)


class Player():  # 定义一个类
    def __init__(self, name, hp, work):
        self.__name = name  # 变量被称作属性
        self.hp = hp
        self.work = work

    def print_role(self):  # 定义一个方法
        print('%s: %s %s' % (self.__name, self.hp, self.work))

    def updateName(self, newname):
        self.__name = newname


class Monster():
    '定义怪物类'
    pass


user1 = Player('tom', 100, 'war')   #类的实例化
user2 = Player('jerry', 80, 'master')
user1.print_role()

user1 .updateName('wilson')
user1.print_role()
user1.name = ('aaa')
user1.print_role()