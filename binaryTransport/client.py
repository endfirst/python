import socket
import struct
import time

# https://docs.python.org/2/library/struct.html

'''
a = '111'
print a
b = a.encode()
print b

c = [ '\0x52', '\0x45']

b = b'111'
print b
print b[0]

a = b'AB'
print a

a = b'\x52\x45'
print a
'''

'''
def sendingMsg():
	data = input()
	data = bytes(data, "utf-8")
	s.send(data)

def gettingMsg():
	data = s.recv(1024)
	data = str(data).split("b'", 1)[1].rsplit("'",1)[0]
	print(data)

HOST = "172.10.12.126"
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (HOST, PORT) )

sendingMsg()
gettingMsg()

s.close()
'''

'''
HOST = "172.10.12.126"
PORT = 20082
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (HOST, PORT) )


size = '000010'
action = 'AUTH'
id = 'id'
cs = '\x11'
pw = 'pw'
end = '\xff'
print cs
print end

a =  struct.pack("!6s4s2sc2sc", size, action, id, cs, pw, end)
print len(a)
print a
s.send(a)
print 'send end'
data = s.recv(1024)
print 'recv end'
print data
'''

# Client Protocol
HOST = "172.10.12.126"
PORT = 20081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (HOST, PORT) )

version = '\x00\x02'
size = '\x00\x00\x00\x0A'
action = 'AUTH'
id = 'id'
cs = '\x11'
pw = 'pw'
end = '\xff'
data = action + id + cs + pw + end
dataLen = len(data)
bSize = struct.pack('!i', dataLen)
totalData = version + bSize + data
print totalData
s.send(totalData)
data = s.recv(6)
size = struct.unpack('!i', data[2:6])
print size[0]
length = size[0]
i = 0
totalData = ""
while(i != length) :
    part = s.recv(length - i)
    i = i + len(part)
    totalData = totalData + part

print 'receive data : [%s]' %totalData

i = "00abcd"
j = i[2:6]
print j



'''
# Provider Protocol
HOST = "172.10.12.126"
PORT = 20082
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (HOST, PORT) )

number = 13
stringSTR = str(number)
stringREPR = repr(number)
print stringSTR
print stringREPR


endfirst = '%6d' %number
print endfirst
endfirst = '%-6d' %number
print endfirst
endfirst = '%06d' %number
print endfirst

number = 10
size = '%06d' %number # size = '000010'
action = 'AUTH'
id = 'id'
cs = '\x11'
pw = 'pw'
end = '\xff'
print cs
print end
data = size + action + id + cs + pw + end
print data

s.send(data)
data = s.recv(6)
print data
length = int(data) # long(data), float(data)
i = 0
totalData = ""
while(i != length) :
    part = s.recv(int(data) - i)
    i = i + len(part)
    totalData = totalData + part

print 'receive data : [%s]' %totalData
'''


'''
zero = '\x30' #0
one = '\x31' #1
two = '\x32' #2
print zero
print one
print two
'''