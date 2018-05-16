# -*- coding:utf-8 -*-
__date__ = '2018/5/14 11:00'

import time
import random
import threading

url_list = []


def get_url(url_list):
    a = random.randint(range(10))
    url_list.append(a)
    time.sleep(2)


def get_html_detial(url_list):
    while True:
        if len(url_list) > 0:
            url = url_list.pop()
            time.sleep(3)
            print(url)


if __name__ == "__main__":
    thread_detail_url = threading.Thread()
