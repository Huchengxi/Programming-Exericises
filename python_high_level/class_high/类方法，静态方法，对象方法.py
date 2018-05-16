# -*- coding:utf-8 -*-


class Date:

    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        # 只能修改对象属性
        self.day += 1
        # 修改类属性
        # Date.day += 1

    # 静态方法实现日期格式的初始化,不好的地方是硬编码，如果类名改了就不适用了
    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split("-"))
        return Date(int(year), int(month), int(day))

    # 类方法
    @classmethod
    def from_string(cls, data_str):
        year, month, day = tuple(data_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


if __name__ == "__main__":
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()
    print(new_day)

    # 2018-12-31
    data_str = "2018-12-31"
    year, month, day = tuple(data_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化
    new_day = Date.parse_from_string(data_str)
    print(new_day)

    # 用classmethod完成初始化
    new_day = Date.from_string(data_str)
    print(new_day)