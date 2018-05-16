# -*- coding:utf-8 -*-
import contextlib


@contextlib.contextmanager
def file_name(file_name):
    print("file_opne")  # enter 中的逻辑
    yield {}
    print("file end")  # exit 中的逻辑


with file_name("1.txt") as f:
    print("file_processing")