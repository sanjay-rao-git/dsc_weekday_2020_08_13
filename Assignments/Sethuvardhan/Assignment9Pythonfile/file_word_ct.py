import sys
import re
import string

k = sys.argv

if len(k) >=2:
	with open(k[1],'r') as fl:
		data_w = fl.read()
	#words = re.split(string.whitespace,data_w)
	words = data_w.split()
	print(words)
	print(len(words))