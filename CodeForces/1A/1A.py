import sys
import math

for line in sys.stdin:
	paras = str(line).split()
	n = int(paras[0])
	m = int(paras[1])
	a = int(paras[2])
	
	print(math.ceil(n/a) * math.ceil(m/a))
