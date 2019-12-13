# -*-coding:utf-8-*-
import os
import re
import time

tickstart = time.time()
path = "C:/Users/xietong/Desktop/repeat/"
path_r = "C:/Users/xietong/Desktop/repeat_r/"
print(path)
# file_no = 'norefund.txt'
file_r = os.listdir(path)
file_write_f = open(path_r + "RF/rf.txt",'w')
file_write_p = open(path_r + "RP/rp.txt",'w')
file_write_s = open(path_r + "RS/rs.txt",'w')
# i=1
i=1
j=1
k=1
for file in file_r:
	if os.path.isdir(path+file):
		print('this is a dir')
	file_read = open(path+file,encoding='utf-8')
	lines = file_read.readlines()
	for line in lines:
		if str('RF') in str(line):
			print('RF   '+str(i))
			file_write_f.writelines(line)
			i=i+1
		elif str('RP') in str(line):
			print('RP   '+str(j))
			file_write_p.writelines(line)
			j=j+1
		elif str('RS') in str(line):
			print('RS   '+str(k))
			file_write_s.writelines(line)
			k=k+1
	file_read.close()
o = i + j + k
file_write_f.close()
file_write_f.close()
file_write_f.close()
print('completed   ' + str(o))
print('start find order norefund')
# time.sleep(3)
# name = 'RS/rs.txt'
# c=0
# # file_read_rec = os.listdir(path_r)
# file_read_rf = open(path_r+'RF/rf.txt',encoding='utf-8')
# lines_rf = file_read_rf.readlines()
# file_read_rp = open(path_r+'RP/rp.txt',encoding='utf-8')
# lines_rp = file_read_rp.readlines()
# file_read_rs = open(path_r+name,encoding='utf-8')
# lines_rs = file_read_rs.readlines()
# file_write_rf = open(path+'汇总.txt','w')
# # file_write_rp = open(path+'汇总.txt','w')

# for line in lines_rf:
# 	line_array = re.split(',',str(line))
# 	print('rf.txt')
# 	print(line_array[2])
# 	if line_array[2] not in str(lines_rs):
# 		c=c+1
# 		file_write_rf.writelines(line_array[2] + "   "+line_array[3])
# 		# file_write_rf.write('\n')
# 		print('\n')
# 		print(c)
# 		print('nonono')
# file_write_rf.write('\n')
# for line in lines_rp:
# 	line_array = re.split(',',str(line))
# 	print('rp')
# 	print(line_array[2])
# 	if line_array[2] not in str(lines_rs):
# 		c=c+1
# 		file_write_rf.writelines(line)
# 		# file_write_rp.write('\n')
# 		print('\n')
# 		print(c)
# 		print('nonono')

# print(c)






















# for file in file_r:
# 	if file in file_no:
# 		continue
# 	# print(file + " " + )
# 	file_index = open(path+"/pidcf.txt")
# 	lines = file_index.readlines()
# 	file_read = open(path + "/" + file,encoding='utf-8')
# 	file_read_line = file_read.readlines()
# 	i = 1
# 	for line in lines:
# 		print(file +" " + str(i) + " " + line)
# 		# print(line)
		
# 		# print(file_read_line)
# 		# print(line)
# 		for file_line in file_read_line:

# 			if str(line).strip() in str(file_line):
# 				print('co')
# 				file_write.writelines(file_line)
# 				file_write.write('\n')
# 		i = i + 1
# 	file_read.close()
# 	file_index.close()
# file_write.close()
# tickend = time.time()
# print(tickend-tickstart)
# t = tickend - tickstart
# t1 = round(t)/60/60
# print('using :' + t1 +'h')

