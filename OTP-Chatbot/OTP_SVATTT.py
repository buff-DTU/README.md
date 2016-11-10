import telnetlib
import socket
import struct
import time
import re 
from gmpy2 import gcd 
from itertools import permutations

host = "chatbot.svattt.org"
port = 5555
s = socket.create_connection((host, port))
msg = s.recv(1024)
msg = s.recv(1024)
#def b2n(b): 
#        return int(b.encode('hex'),16)
enc_list = []
greet = [2842744914241024623, 6841721, 46653803623210, 595997967067779695967913763258456464489608998975]
for i in range(0,20):
	s.send("hello\n")
	msg = s.recv(1024)
	enc_list.append(msg)
	msg = s.recv(1024)
enc_list = set(enc_list)
print enc_list
powgreet = []
e = 0x10001
temp_encrypt_key=[]
for i in range(len(greet)):
	powgreet.append(pow(greet[i], e))
for (a,b,c,d) in list(permutations(enc_list, 4)):
	temp = gcd(powgreet[0]-int(a),gcd(powgreet[1]-int(b),gcd(powgreet[2]-int(c),powgreet[3]-int(d))))
	temp_encrypt_key.append(temp)
print temp_encrypt_key
print "encrypt_key ======",max(temp_encrypt_key)
s.send("FLAG?\n")
msg = s.recv(1024)
print "enc_flag======",msg

s.close()
