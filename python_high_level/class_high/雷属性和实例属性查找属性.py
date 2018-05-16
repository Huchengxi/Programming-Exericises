# -*- coding:utf-8 -*-


class A:
    name = "A"

    def __init__(self):
        self.name = "obj"


a = A()
print(a.name)

# MRO算法，从左往右，自下而上经典类(深度优先)
# 新式类，广度优先
# C3算法 现在的MRO为C3算法

class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)