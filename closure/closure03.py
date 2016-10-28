# -*- coding: utf-8 -*-

def outer_func(): #1
    message = 'Hi' #3

    def inner_func(): #4
        print message #6

    return inner_func #5

my_func = outer_func() #2

print my_func