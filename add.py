#coding:utf8
import os
import getpass
# path to shadowsocks gfwlist file
path = "/Users/"+getpass.getuser()+"/.ShadowsocksX/gfwlist.js"

def add(rule):
	with open(path,'r') as f:
		buf = f.readlines()
	with open(path,'w') as f:

		for i,line in enumerate(buf):
			# it works for me
			if i == 6:
				f.write("\""+rule+"\",\n")
				f.write(line)
			else:
				f.write(line)


if __name__ == "__main__":
	test('baidu.com')
