import sys

for line in sys.stdin:
    paras = str(line).strip().split()
    m = int(paras[0])
    n = int(paras[1])
    print(int((m*n)/2))
