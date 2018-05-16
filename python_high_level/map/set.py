# -*- coding:utf-8 -*-
__date__ = '2018/5/6 17:06'
# set 集合 fronzenset(不可变集合)，不重复，无序
from copy import deepcopy
data_list = []
default_data = {
    "a": 1,
    "b": 2
}

default_data.update({"c": 3})
data = deepcopy(default_data)
data_list.append(data)
default_data.update({"c": 4})
data = deepcopy(default_data)
data_list.append(data)
print(data_list)