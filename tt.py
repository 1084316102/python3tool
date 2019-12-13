# -*-coding:utf-8-*-
import os

path = "C:/Users/xietong/Desktop/p3"
print(path)
file_no = ['Лузм.txt','pidcf.txt','test.txt']
file_r = os.listdir(path)
file_write = open(path + "/test.txt",'w')
for file in file_r:
	if file in file_no:
		continue
	# print(file + " " + )
	file_index = open(path+"/pidcf.txt")
	lines = file_index.readlines()
	file_read = open(path + "/" + file)
	for line in lines:
		print(file + " " + line)
		# print(line)
		file_read_line = file_read.readline()
		if line in file_read_line:
			file_write.writelines(file_read_line)
			file_write.write('\n')
	file_read.close()
	file_index.close()

	