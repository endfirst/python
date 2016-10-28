# -*- coding: utf-8 -*-

# 클로저는 이렇게 하나의 함수로 여러가지의 함수를 간단히 만들어낼 수 있게도 해주며,
# 기존에 만들어진 함수나 모듈등을 수정하지 않고도 wrapper 함수를 이용해 커스터마이징할 수 있게 해주는 기특한 녀석입니다.



def outer_func(tag):  #1
    tag = tag  #5

    def inner_func(txt):  #6
        text = txt  #8
        print '<{0}>{1}<{0}>'.format(tag, text)  #9

    return inner_func  #7

h1_func = outer_func('h1')  #2
p_func = outer_func('p')  #3

h1_func('h1태그의 안입니다.')  #4
p_func('p태그의 안입니다.')  #10