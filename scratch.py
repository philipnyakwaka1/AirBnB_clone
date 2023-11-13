#!/usr/bin/python3
def my_func(*args, **kwargs):
    print(kwargs)


my_func(name="Philip", age="25")
