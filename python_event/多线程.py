# -*- coding:utf-8 -*-
from multiprocessing.pool import ThreadPool


def foo(bar, baz):
    print "hello {0}".format(bar)
    return 'fo0' + baz


pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ("xiaorui.cc", "foo"))

return_val = async_result.get()



# print async_result