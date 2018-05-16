# -*- coding:utf-8 -*-


def func(a: 'spam', b: (1, 10), c: float)->int:
    print(func.__annotations__)
    return a+b+c

c = func(1, 2, 3)

print(c)

