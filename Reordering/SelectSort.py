# -*- coding:utf-8 -*-
def select_short(list):
    # 选择排序
    count = len(list)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if list[min] > list[j]:
                min = j
            list[min], list[i] = list[i], list[min]
    return list


if __name__ == "__main__":
    list = [89, 98, 77, 66, 0, 29, 23]
    select_short(list)
    print(list)
