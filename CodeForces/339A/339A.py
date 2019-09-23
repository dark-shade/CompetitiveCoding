import sys

for line in sys.stdin:
	nums = line.strip().split('+')
	nums.sort()
	print('+'.join(nums))
	break
