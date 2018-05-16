# -*- coding:utf-8 -*-

# 函数和类也是对象，属于python的一等公民
# 1. 可以赋值给一个对象
# 2. 可以添加到集合中
# 3. 可以作为参数传递给函数
# 4. 可以当做函数的返回值


def ask(name="hu"):
    print(name)


class Person:
    def __int__(self):
        print("huyanwei")

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())


# my_func = ask
# my_func()
#
#
# my_class = Person
# my_class()


# 对像的三个特征
# 1. 身份 内存地址 2. 类型 3. 值
# 数值类型， None类型（全局只有一个）， 迭代类型， 序列类型(list,bytes,range,tuple,str,array)， 映射， 集合， 上下文管理类型， 其他。
# 模块类型， class和实例， 函数类型， 方法类型， 代码类型， object对象， type类型，ellipsis类型, notimplemented类型







































