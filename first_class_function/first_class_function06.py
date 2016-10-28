# -*- coding: utf-8 -*-
def logger(msg):

    def log_message(): #1
        print 'Log: ', msg

    return log_message

log_hi = logger('Hi')
print log_hi # log_message 오브젝트가 출력됩니다.
log_hi() # "Log: Hi"가 출력됩니다.

del logger # 글로벌 네임스페이스에서 logger 오브젝트를 지웁니다.

# logger 오브젝트가 지워진 것을 확인합니다.
try:
    print Logger
except NameError:
    print 'NameError: Logger는 존재하지 않습니다.'

log_hi() # Logger가 지워진 뒤에도 Log: Hi"가 출력됩니다.