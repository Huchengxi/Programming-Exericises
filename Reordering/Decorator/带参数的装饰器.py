# -*- coding:utf-8 -*-


def w1(num):
    print(num)

    def w2(func):

        def inner(*args, **kwargs):
            print("带参数的装饰器！")
            return func(*args, **kwargs)
        return inner
    return w2


@w1(2)
def test(num):
    print(num)

a = 3

test(3)