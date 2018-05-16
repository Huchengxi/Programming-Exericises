# -*- coding:utf-8 -*-
__date__ = '2018/4/26 13:57'


i = 1
while i <= 9:
    j = 1
    while j <=i:
        print("%s * %s = %s " % (i, j, i*j), end='')
        j += 1
    print("\n")
    i += 1