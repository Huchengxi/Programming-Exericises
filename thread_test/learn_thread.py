# -*- coding:utf-8 -*-
import time
import threading
from threading import Lock
from Queue import Queue

detail_url_list = ["1", "2", "3"]

flag = True


def get_detail_html(queue, lock):
    global flag
    while True:
        url = queue.get()
        print url
        print "get detail html started"
        time.sleep(2)
        print "get detail html end"
        lock.acquire()
        flag = False
        lock.release()
        # raise NameError
        if queue.empty():
            break


def get_detail_url(queue, lock):
    global flag
    print "get detail url started"
    time.sleep(4)
    for i in range(20):
        lock.acquire()
        flag = True
        lock.release()
        queue.put("http://test.com/{id}".format(id=i))
    print "get detail url end"


if __name__ == "__main__":
    tt_list = []
    url_queue = Queue(maxsize=1000)
    lock = Lock()
    thread_detail_url = threading.Thread(target=get_detail_url, args=(url_queue, lock))
    thread_detail_url.start()
    # thread_detail_url.join()
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(url_queue, lock))
        html_thread.start()
        tt_list.append(html_thread)
        # html_thread.join()
    for tt in tt_list:
        tt.join()
    ip_list = ["1", "2", "3", "4"]
    ip_queue = Queue()
    for ip in ip_list:
        ip_queue.put(ip)
    print ip_queue