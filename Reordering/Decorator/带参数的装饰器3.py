# -*- coding:utf-8 -*-


def w1(w):
    def inner(func):
        print("22")
        print(w)
        print(func.__code__.co_varnames)
        return func
    return inner


@w1(11)
def test(num, num2):
    return num*num2


c = test(2, 3)
print(c)