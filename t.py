# -*-coding:utf-8-*-
import os
file_obj = open("test2.txt")
all_lines = file_obj.readlines()
for line in all_lines:
  print line
file_obj.close()
# 写之前，先检验文件是否存在，存在就删掉
if os.path.exists("dest.txt"):
  os.remove("dest.txt")
mylist = ["luoluo", "taotao", "mumu"]
# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open("dest.txt", 'w')
for var in mylist:
  file_write_obj.writelines(var)
  file_write_obj.write('\n')
file_write_obj.close()