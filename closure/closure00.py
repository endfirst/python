# -*- coding: utf-8 -*-


# 클로저는 코드를 데이터로 취급하며, 정교한 매크로 시스템을 갖고 있다.
# 클로저란 네임 바인딩 기술이다.
# 클로저는 일반 함수와는 다르게, 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한 뒤, 이 캡처한 값들에 액세스할 수 있게 도와준다.

def outer_func(): #1
    message = 'Hi' #3

    def inner_func(): #4
        print message #6

    return inner_func() #5

outer_func() #2