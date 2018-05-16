# -*- coding:utf-8 -*-

class A:
    pass

class B(A):
    pass


b = B()
# isinstance会自动搜寻继承链
print(isinstance(b, B))
print(isinstance(b, A))

print(type(b) is B)
print(type(b) is A)

