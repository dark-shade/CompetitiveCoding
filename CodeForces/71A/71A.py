import sys

num = 0

for line in sys.stdin:
	if num == 0:
		num = int(line)
		continue
	word = str(line).strip()
	if len(word) > 10:
		print(word[0] + str(len(word)-2) + word[-1])
	else:
		print(word)
