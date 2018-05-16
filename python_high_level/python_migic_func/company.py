# -*- coding:utf-8 -*-


class Company:
    def __init__(self, employee_list):
        self.a = employee_list

    def __getitem__(self, item):
        return self.a[item]

    def __len__(self):
        return len(self.a)

employee_list = ["tom", "bob", "jane"]

company = Company(employee_list)

# employee = company.a

for em in company:
    print(em)

print(company[::-1])
