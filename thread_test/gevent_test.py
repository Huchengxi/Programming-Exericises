# -*- coding:utf-8 -*-
__date__ = '2018/5/14 13:17'
from gevent import monkey; monkey.patch_socket()
import gevent
import time
from Queue import Queue
i = 0


def get_url(queue):
    while True:
        print "get html detail started"
        url = queue.get()
        print "url %s" % url
        time.sleep(2)
        if queue.empty():
            break


def get_html_detail(queue):
    # global i
    # i += 1
    # queue.put(i)
    # time.sleep(1)
    print "get url started"
    time.sleep(3)
    for i in range(20):
        queue.put(i)
    print "get url end"


if __name__ == "__main__":
    url_queue = Queue()
    gevent.joinall([
        gevent.spawn(get_html_detail, url_queue),
        gevent.spawn(get_url, url_queue),
        gevent.spawn(get_url, url_queue),
    ])