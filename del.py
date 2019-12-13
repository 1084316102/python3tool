# -*-coding:utf-8-*-
import os
import re
import time
import csv

path = "C:/Users/xietong/Desktop/201909_11_all/"
# file = open(path+'汇总.txt',encoding='utf-8')


# get dict
all = {}

with open(path+'汇总.txt',encoding='utf-8') as file_all:
	for line in file_all.readlines():
		if not line:
			continue
		# line = line.strip()
		# line_arr = line.split(',')
		line_arr = re.split(',',str(line))
		if len(line_arr) == 1:
			continue
		print(len(line_arr))
		order_id = line_arr[2]
		all[order_id] = line
		print(order_id)

# print(all)

#del
with open(path+"all.csv",'w') as file_write:
	# w = csv.DictWriter(file_write,all.keys())
	# w.writerow(all)
	 [file_write.write('{0},{1}'.format(key, value)) for key, value in all.items()]
	# file_write.writelines(all)