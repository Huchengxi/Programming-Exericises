# -*- coding:utf-8 -*-
import time
from collections import deque
from random import Random
import threading


class Example():

    def __init__(self):
        self.r = Random(time.time())

    def worker_run(self, name, q):
        while True:
            if q:
                print("%s pop number: %s, %s numbers left" % (name, q.pop(), len(q)))
            time.sleep(0.001)

    def manager_run(self, worker_num):
        queue_list = [deque() for i in range(worker_num)]

        worker_list = [threading.Thread(target=self.worker_run,
                                        args=["Thread-%s" % i, queue_list[i]]) for i in range(worker_num)]
        for worker in worker_list:
            worker.start()
        while True:
            i = 0
            while i < self.r.randint(0, 20):
                queue_list[self.r.randint(0, worker_num - 1)].appendleft(
                    self.r.randint(1, 100)
                )
                i += 1
            time.sleep(self.r.random() / 100)


if __name__ == '__main__':
    Example().manager_run(3)

