#!/usr/bin/env python
# coding=utf-8

def foo():
    a = 1
    def bar():
        nonlocal a
        a = a + 1
        print("bar()a=", a)
    bar()
    print("foo()a=", a)

foo()
