# -*- coding:utf-8 -*-


class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)
# 从下往上查找的原则，会优先查找对象本身的属性
A.aa = 11
a.aa = 100
print(a.x, a.y, a.aa)
print(A.aa)
