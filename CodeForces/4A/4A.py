import sys

for line in sys.stdin:
	if int(line) % 2 == 0 and int(line) != 2:
		print("YES")
	else:
		print("NO")
