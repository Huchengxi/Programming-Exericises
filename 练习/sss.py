# -*- coding:utf-8 -*-
__date__ = '2018/4/26 18:08'


def res(data):
    l = len(data)
    for i in range(0, int(l/2)):
        data[i], data[l-i-1] = data[l-i-1], data[i]
    return data

# data = [1, 2, 3, 5]
# print(res(data))


def res_str(strs):

    str_list = []
    for i in strs:
        str_list.append(i)
    str_list = res(str_list)
    str_list = "".join(str_list)
    return str_list


def res2(data):
    lists = []
    l = len(data)-1
    while l >= 0:
        lists.append(data[l])
        l -= 1
    return lists


def res3(data):
    lists = []
    for _ in range(len(data)):
        lists.append(data.pop())
    return lists

print(res3([1,2,3,4]))