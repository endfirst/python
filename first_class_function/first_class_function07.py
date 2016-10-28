# -*- coding: utf-8 -*-
# 단순한 일반 함수
def simple_html_tag(tag, msg):
    print '<{0}>{1}<{0}>'.format(tag, msg)

simple_html_tag('h1', '심플 헤딩 타이틀')

print '-'*30

# 함수를 리턴하는 함수
def html_tag(tag):

    def wrap_text(msg):
        print '<{0}>{1}<{0}>'.format(tag, msg)

    return wrap_text

print_h1 = html_tag('h1') #1
print print_h1 #2
print_h1('첫 번째 헤딩 타이틀') #3
print_h1('두 번째 헤딩 타이틀') #4

print_p = html_tag('p')
print_p('이것은 패러그래프 입니다.')