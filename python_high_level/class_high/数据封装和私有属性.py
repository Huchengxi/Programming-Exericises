# -*- coding:utf-8 -*-


# 实现私有属性和私有方法
class User:
    def __init__(self, birthday):
        self.birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.birthday.year


if __name__ == "__main__":
    user = User()
    # print(_classname__attrname) 并不是从语言的层面上私有，将名变形