# -*- coding:utf-8 -*-
import os
import re
from time import sleep
#插上u盘时遍历所有文件
def simple_dir_tree(ddir):
	tree=open('tree.txt','w',encoding='utf-8')
	for dirpath,dirnames,filenames in os.walk(ddir.strip(os.sep)):
		dirn = os.path.basename(dirpath)
		string = ' '*len(os.path.dirname(dirpath)) + '|-' + dirn
		for f in filenames:
			try:
				string = string + '\n' + ' '*len(dirpath) + '|-' + str(f)+'('+ str(os.path.getsize(os.path.join(dirpath,f))/float(1024*1024)).split('.')[0] +'MB)'
				tree.write(string)
			except Exception as e:
				pass
	tree.close()
	exit()
def monitoring():
	while True:
		if os.path.exists("F:"):
			simple_dir_tree("F:")
		sleep(5)
if __name__ == "__main__":
	monitoring()