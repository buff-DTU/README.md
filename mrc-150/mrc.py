import subprocess
import re
key = "ffc309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e"
flag = ""
a = 1
s = ""
for i in range(32,127):
	s += chr(i)
while 1:
	for i in s:
		f = open("flag.txt","w")
		f.write(flag+i)
		f.close()
		p = subprocess.Popen(['./mrc', "flag.txt"], stdout=subprocess.PIPE) 
		p.wait()
		buf = p.stdout.read().decode('ascii')
		so = key[a*2:a*2+2]
		buf1 = buf[len(buf)-3:-1]
		if buf1 == so:
			flag+=i
			break
	
	a += 1
	print "temp:",flag
print "flag is:",flag

		
