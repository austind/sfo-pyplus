#!/usr/bin/env python

def my_func(x, y, z=20):
    return x + y + z

print(my_func(10, 15, 30))
print(my_func(10, 15))
print(my_func(10, y=15, z=30))
print(my_func('happy ', 'days ', 'ahead'))
print(my_func(['happy'], ['days'], ['ahead']))
