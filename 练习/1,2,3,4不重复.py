# -*- coding:utf-8 -*-
__date__ = '2018/4/26 14:25'
c = 0
lists = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                lists.append(i*100 + k*10 + j)
                c += 1
                print(c)
print(lists)


