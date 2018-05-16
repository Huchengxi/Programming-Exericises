# -*- coding:utf-8 -*-

# 魔法函数其实是数据模型的一种叫法，增强类型
# 魔法函数并不是继承于其他任何类的， 有python解释器默认调用
# 字符串表示


class Company:

    def __init__(self, employee_list):
        self.employee = employee_list

    # 对字符串格式化
    def __str__(self):
        return ",".join(self.employee)

    # 公开发人员是使用
    def __repr__(self):
        return ",".join(self.employee)

company = Company(["tom", "toony", "hu"])


print(company)