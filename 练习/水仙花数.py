# -*- coding:utf-8 -*-
__date__ = '2018/4/26 14:43'

lists = []
for n in range(100, 1001):
    i = n/100
    j = n/10 % 10
    k = n % 10
    if i * 100 + j * 10 + k == i + j ** 2 + k ** 3:
        lists.append(n)

print(lists)