import sys

n = 0
k = 0

for line in sys.stdin:
	paras = str(line).split()
	if n == 0 and k == 0:
		n = int(paras[0])
		k = int(paras[1])
		continue
	
	cnt = 0
	next_cnt = 0

	for score in paras:
		if int(score) >= int(paras[k-1]) and int(score) > 0:
			next_cnt += 1
		else:
			break

	print(next_cnt)	
