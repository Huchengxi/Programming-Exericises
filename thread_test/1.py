# -*- coding:utf-8 -*-
a_list = [2, 23, 3, 6, 1]


# for i in range(len(a_list)):
#     for j in range(1, len(a_list)):
#         if a_list[j] < a_list[j-1]:
#             a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
for i in range(len(a_list)):
    for j in range(i+1, len(a_list)):
        if a_list[i] > a_list[j]:
            a_list[i], a_list[j] = a_list[j], a_list[i]


print a_list