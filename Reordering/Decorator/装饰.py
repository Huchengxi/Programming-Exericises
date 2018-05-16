# -*- coding:utf-8 -*-


def w1():
    def inner(func):
        print("开始验证")
        # print(inner.__code__.co_varnames, "222")
        # print(func.__code__.co_varnames)
        return func
    return inner


@w1()
def test(num):
    b = num
    return b


a = 2
c = test(a)
print(c)
