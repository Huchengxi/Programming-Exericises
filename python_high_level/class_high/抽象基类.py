# -*- coding:utf-8 -*-

# 抽象基类，类似于Java中的接口

# 1. 检查某个类是否有某种方法, hasattr方法


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["a", "b", "c"])
print(len(company))
print(hasattr(company, "__len__"))

# 1. 我们需要在某些情况之下希望判定某个对象的类型
# 2. 我们需要某一个子类必须实现某些方法
from collections.abc import Sized
isinstance(company, Sized)

# 如何去模拟一个抽象基类
# class CacheBase:
#     def get(self, get):
#         raise NotImplemented
#
#     def set(self, key, value):
#         raise NotImplemented
#
#
# class RedisCache(CacheBase):
#     pass
#
# redis_cache = RedisCache()
# redis_cache.set(1, 2)

# 希望在初始化的时候就检查是否重写抽象基类的方法而不是调用的时候才会发现
import abc
class CaCheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, get):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class MyCaChe(CaCheBase):
    pass

a = MyCaChe()