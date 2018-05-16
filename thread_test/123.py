# -*- coding:utf-8 -*-
import time
import threading
from Queue import Queue
from concurrent.futures import ThreadPoolExecutor
excutor = ThreadPoolExecutor(max_workers=2)

detail_url_list = []


def get_detail_html(queue):
    while True:
        url = queue.get()
        print url
        print "get detail html started"
        time.sleep(2)
        print "get detail html end"

task1 = excutor.submit(get_detail_html, (queue))

for data in excutor.map(get_detail_html, queue):
    # data = future.result()
    print data


def get_detail_url(queue):
    print "get detial url started"
    time.sleep(4)
    for i in range(20):
        queue.put("http://test.com/{id}".format(id=i))
    print "get detail url end"


if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        html_thread.start()
    detail_url_queue.task_done()
    detail_url_queue.join()