import sys

num_of_problems = 0
cnt = 0

for line in sys.stdin:
	if num_of_problems == 0:
		num_of_problems = int(str(line).strip())
		continue

	paras = str(line).strip().split()

	inner_cnt = 0

	for para in paras:
		if para == '1':
			inner_cnt += 1
	if inner_cnt > 1:
		cnt += 1

	num_of_problems -= 1

	if num_of_problems == 0:
		break

print(cnt)		
