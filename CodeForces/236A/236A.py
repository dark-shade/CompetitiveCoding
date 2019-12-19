import sys

for line in sys.stdin:
	unique_chars = set(line.strip())
	if len(unique_chars) % 2 == 0:
		print("CHAT WITH HER!")
	else:
		print("IGNORE HIM!")
	break
