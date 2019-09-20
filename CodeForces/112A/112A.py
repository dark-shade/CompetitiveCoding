import sys

strings = []
cnt = 2

for line in sys.stdin:
    strings.append(line.strip().lower())
    cnt -= 1
    if cnt == 0:
         break
if strings[0] > strings[1]:
    print("1")
elif strings[0] < strings[1]:
    print("-1")
else:
    print("0")
