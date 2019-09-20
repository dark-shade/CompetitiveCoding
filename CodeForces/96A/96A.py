import sys

for line in sys.stdin:
    cnt = 0
    prev = ""
    
    for ch in line.strip():
        if len(prev) == 0:
            prev = ch
            cnt += 1
            continue
        if ch == prev:
            cnt += 1
        else:
            prev = ch
            cnt = 1

        if cnt == 7:
            print("YES")
            break
    if cnt != 7:
        print("NO")

    break

