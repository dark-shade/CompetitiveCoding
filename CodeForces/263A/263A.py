import sys

row = 0
col = 0
cnt = 0

for line in sys.stdin:
	cnt += 1

	if "1" in line:
		row = cnt
		col = line.strip().split().index('1') + 1
		
		moves = abs(row - 3) + abs(col - 3)
		print(moves)
		break			
