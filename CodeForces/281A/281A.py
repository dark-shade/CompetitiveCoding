import sys

for line in sys.stdin:
	cap_line = line[0].upper() + line.strip()[1:]
	print(cap_line)
	break
