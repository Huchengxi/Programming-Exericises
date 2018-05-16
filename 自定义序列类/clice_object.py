# -*- coding:utf-8 -*-
__date__ = '2018/5/5 22:39'
import numbers


class Group:
    # 支持切片操作
    def __init__(self, name, company_name, staffs):
        self.group_name = name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.revers()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        return False

