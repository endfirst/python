# -*- coding: utf-8 -*-
def square(x):
    return x * x

num_list = [1, 2, 3, 4, 5]

def simple_square(arg_list):
    result = []
    for i in arg_list:
        result.append(i * i)
    return result

simple_squares = simple_square(num_list)

print simple_squares