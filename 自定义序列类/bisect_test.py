# -*- coding:utf-8 -*-
__date__ = '2018/5/5 23:05'

import bisect

# 用来处理已排序的序列 的查找模块 支持可变序列
# 用的是二分查找
inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 4)
bisect.insort(inter_list, 1)
print(bisect.bisect(inter_list, 3))  # 默认插入到已重复元素的右边，bisect_left
print(inter_list)


