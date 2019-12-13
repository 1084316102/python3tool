#-*-coding:utf-8-*-
import os
import re
import time

path = 'C:/Users/xietong/Desktop/201909_11_all/'

with open(path+'201909_11_all.csv',encoding='utf-8') as file_read:
	lines = file_read.readlines()
	file_write = open(path+'rs.csv','w')
	for line in lines:
		if str('RS') not in str(line):
			continue
		print(line)
		file_write.writelines(line)
	file_write.close()
print('completed')