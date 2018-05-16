# -*- coding:utf-8 -*-
def insert_sort(list):
    # 插入排序
    count = len(list)
    for i in range(1, count):
        key = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1
    return list


if __name__ == "__main__":
    list = [90, 20, 80, 25, 33]
    insert_sort(list)
    print(list)
    