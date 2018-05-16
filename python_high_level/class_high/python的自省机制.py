# -*- coding:utf-8 -*-

# 自省是通过一定的机制查询到对象的内部结构


class Person:
    """
    人
    """
    name = "user"


class Student(Person):
    def __init__(self, s_n):
        self.s_n = s_n


if __name__ == "__main__":
    user = Student("慕课网")

    # 通过__dict__查询属性
    print(user.__dict__)
    user.__dict__["s_d"] = "北京市"
    print(user.s_d)
    print(Person.__dict__)
    print(user.name)  # name 属于Person的类对象的属性
