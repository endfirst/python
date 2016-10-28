# -*- coding: utf-8 -*-

def outer_func():  #1
    message = 'Hi'  #3

    def inner_func():  #4
        print message  #6

    return inner_func  #5

my_func = outer_func()  #2

print my_func  #7
print
print dir(my_func)  #8
print
print type(my_func.__closure__) #9
print
print my_func.__closure__  #10
print
print my_func.__closure__[0]  #11
print
print dir(my_func.__closure__[0])  #12
print
print my_func.__closure__[0].cell_contents  #13