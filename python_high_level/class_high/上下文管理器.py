# -*- coding:utf-8 -*-

# with
# 上下文管理器协议， 魔法函数类似协议


class Sample:
    def __enter__(self):
        # 获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("do_something")


with Sample() as sample:
    sample.do_something()

