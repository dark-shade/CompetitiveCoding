import sys

x = 0
num_of_ops = 0

for line in sys.stdin:
    if num_of_ops == 0:
        num_of_ops = int(str(line).strip())
        continue
    if "++" in line:
        x += 1
    if "--" in line:
        x -= 1
    num_of_ops -= 1
    if num_of_ops == 0:
        break
print(x)
