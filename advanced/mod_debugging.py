#-*- coding: utf-8 -*-
u"""
MOD: Debugging
"""
import pdb


def another_func(arg1, arg2):
    print "Another func was called:", arg1, arg2


def func_to_fail():
    my_string = "This is a string"
    my_float = 123.456
    pdb.set_trace()
    another_func(my_string, my_float)
    raise ValueError(13)


def caller_func():
    func_to_fail()


if __name__ == "__main__":
    caller_func()
