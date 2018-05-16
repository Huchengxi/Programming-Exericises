# -*- coding:utf-8 -*-
__date__ = '2018/5/14 15:56'
import threading
import time


def func2():
    time.sleep(1)
    print "-------------"


def func():
    time.sleep(1)
    print "+++++++++++++"

    a = threading.Thread(target=func2)
    a.start()
    b = threading.Thread(target=func2)
    b.start()
    c = threading.Thread(target=func2)
    c.start()
    # a.join()
    # b.join()
    # c.join()


if __name__ == "__main__":
    func()
    print "2"