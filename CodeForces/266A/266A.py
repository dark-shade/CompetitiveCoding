import sys

num_of_rocks = 0

for line in sys.stdin:
	if num_of_rocks == 0:
		num_of_rocks = int(line.strip())
		continue

	prev_ch = ''
	cnt = 0

	for ch in line.strip():
		if ch == prev_ch:
			cnt += 1
		else:
			prev_ch = ch

	print(cnt)
	break

