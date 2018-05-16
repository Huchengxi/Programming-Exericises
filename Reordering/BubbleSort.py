def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def while_bubble_sort(lists):
    # 冒泡排序 while版本？？？？？？ ZZ 这是插入排序！
    count = len(lists)
    i = 0
    while i < count:
        j = 1
        while j < count:
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
            j += 1
        i += 1
    return lists


def while_bubble_sort_really(lists):
    # 真正的冒泡排序while版本
    count = len(lists)
    i = 0
    while i < count:
        j = i + 1
        while j < count:
            if lists[j-1] > lists[j]:
                lists[j-1], lists[j] = lists[j], lists[j-1]
            j += 1
        i += 1
    return lists


if __name__ == '__main__':
    lists = [2, 90, 80, 45, 23, 88]
    while_bubble_sort_really(lists)
    print(lists)
