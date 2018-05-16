# -*- coding:utf-8 -*-
__date__ = '2018/5/5 21:38'

# 1. 容器序列   list,tuple,deque
# 2. 扁平序列   str,bytes,bytearray,array.array
# 3. 可变序列   list,deque,bytearray,array
# 4. 不可变     str,tuple,bytes

from collections import abc

a = [1, 2]

# c = a + (3, 4)
c = a + [3, 4]

# += 就地加,调用的是extend
# a += [3, 4]
a += (3, 4)  # 可以为任意的序列类型

# def extend(self, values):
#     for v in values:
#         self.append(v)


