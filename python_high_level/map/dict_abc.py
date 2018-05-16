# -*- coding:utf-8 -*-
__date__ = '2018/5/6 16:27'

from collections.abc import Mapping, MutableMapping

new_list = ["a", "b", "c"]

new_dict = dict.fromkeys(new_list, "")

print(new_dict)
print(new_dict.items())

new_dict.update([("a", "2")])
from collections import UserDict, defaultdict