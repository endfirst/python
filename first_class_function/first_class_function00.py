# -*- coding: utf-8 -*-

# 퍼스트클래스 함수란 프로그래밍 언어가 함수 (function) 를 first-class citizen으로 취급하는 것을 뜻합니다.
# 쉽게 설명하자면 함수 자체를 인자 (argument) 로써 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴 할수도 있고,
# 함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있는 함수를 뜻합니다.

def square(x):
    return x * x

print square(5)

f = square

print square
print f