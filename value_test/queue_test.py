# -*- coding:utf-8 -*-
__date__ = '2018/5/14 15:28'
from Queue import Queue

test = Queue()
c = {"c": 3}
test.put({"a": 1, "b": 2})
test.put({"c": c.get("c")})
print test.get()
print test.get()["c"]