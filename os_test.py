# -*- coding:utf-8 -*-

import os
import time
import hashlib

def time_stamp_to_time(time_stamp):
    time_struct = time.localtime(time_stamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_struct)


def create_time(path):
    time_stamp = os.path.getctime(path)
    file_create_time = time_stamp_to_time(time_stamp)
    return file_create_time

# i = 0
# for root, dirs, files in os.walk("C:\Programming-Exericises"):
#     for dir_name in dirs:
#        for root1, dirs1, files1 in os.walk(dir_name):
#            print(root1, dirs1, files1)


def get_file(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isdir(file):
                get_file(file)
            else:
                print(hashlib.md5(open('%s' % file).read()).hexdigest())



# rootdir = 'D:\\test'
# print('rootdir = ' + rootdir)

pathname = []

for (dirpath, dirnames, filenames) in os.walk("C:\Programming-Exericises"):
    for filename in filenames:
        pathname += [os.path.join(dirpath, filename)]

print(pathname, len(pathname))