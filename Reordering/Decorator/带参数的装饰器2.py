# -*- coding:utf-8 -*-


def attrs(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    print(getattr(mymethod, "versionadded", 0))
    print(getattr(mymethod, 'author', 0))
    print(f)

mymethod(2)