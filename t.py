# -*-coding:utf-8-*-
import os
file_obj = open("test2.txt")
all_lines = file_obj.readlines()
for line in all_lines:
  print line
file_obj.close()
# д֮ǰ���ȼ����ļ��Ƿ���ڣ����ھ�ɾ��
if os.path.exists("dest.txt"):
  os.remove("dest.txt")
mylist = ["luoluo", "taotao", "mumu"]
# ��д�ķ�ʽ���ļ�������ļ������ڣ��ͻ��Զ�����
file_write_obj = open("dest.txt", 'w')
for var in mylist:
  file_write_obj.writelines(var)
  file_write_obj.write('\n')
file_write_obj.close()