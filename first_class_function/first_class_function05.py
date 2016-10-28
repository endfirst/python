# -*- coding: utf-8 -*-
def logger(msg):

    def log_message(): #1
        print 'Log: ', msg

    return log_message

log_hi = logger('Hi')
print log_hi # log_message 오브젝트가 출력됩니다.
log_hi() # "Log: Hi"가 출력됩니다.