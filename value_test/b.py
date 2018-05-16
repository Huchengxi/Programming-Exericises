# -*- coding:utf-8 -*-
a = 1
b = 1
flag = True


def add():
    global b
    b += 1
    print(b)


def f():
    global F
    F += 1


def func(a):
    a += 1


def func2(a_list):
    a_list.append("1")


def func3(a_dict):
    a_dict.update({"a": 1})


def func4(a_list):
    a_list[0] = True


if __name__ == "__main__":
    a = 2
    func(a)
    print a