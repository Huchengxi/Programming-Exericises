# -*- coding:utf-8 -*-

import os
import operator

def add_log(path):
    with open('out.txt', 'w') as f:
        f.close()
    for root, dirs, files in os.walk(path):
        for name in files:
            temp_path = os.path.join(root, name)
            # file_name = temp_path.replace('C:/Users/Enter/Desktop/', '')
            file_time = os.stat(temp_path).st_mtime
            with open('out.txt', 'a') as f:
                f.write(','.join(['%s' % temp_path, '%s\n' % file_time]))
                f.close()


txt = open('out.txt', 'r').readlines()
myDic = {}
for row in txt:
    (key, value) = row.split(',')
    myDic[key] = value
print(myDic)

# path = "C:\Programming-Exericises"
# add_log(path)