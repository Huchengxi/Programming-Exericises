# -*- coding:utf-8 -*-


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        # python2
        super(B, self).__init__()
        # python3
        super().__init__()

from threading import Thread


class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)


if __name__ == "__main__":
    b = B()