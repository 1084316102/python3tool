# -*- coding: utf-8 -*-
num=0
def getNum(n):
	if n==1:
		return getInit()
	s = getNum(n-1)
	if s%4!=0:
		return -1
	return (s/4)*5 + 1
def getInit():
	global num
	while True:
		if (num % 4 ==0) and (num-1)%5==0:
			return num
		num = num+1
v=-1
while v==-1:
	print(num)
	v=getNum(5)
	num = num + 1
print(v)