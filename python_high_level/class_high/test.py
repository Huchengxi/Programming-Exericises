# -*- coding:utf-8 -*-


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "%s" % self.month

class User:
    def __init__(self, birthday):
        self.birthday = birthday

    def get_age(self):
        return 2018 - self.birthday.year


if __name__ == "__main__":
    print(Date(2, 2, 2))
    user = User(Date(2, 2, 2))
    print(user.get_age())
    print(user.birthday)