# -*- coding:utf-8 -*-
__date__ = '2018/5/5 23:33'
# 列表推到式

# 1. 提取1-20之间的奇数
odd_list = [i for i in range(21) if i % 2 > 0]

# 2. 逻辑复杂的情况


def handle_item(item):
    return item * item


odd_list2 = [handle_item(i) for i in range(21) if i % 2 > 0]
print(odd_list)

# 生成器表达式

odd_list3 = (i for i in range(21) if i % 2 > 0)


# 字典推到是
my_dict = {v: k for k, v in dict.items()}