import sys

for line in sys.stdin:
	paras = str(line).split()
	w = int(paras[0])
	k = int(paras[1])

	while k > 0:
		if w % 10 == 0:
			w = w /10
		else:
			w -= 1
		k -= 1
	print(int(w))
