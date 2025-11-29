import sys
v1, v2 = map(int, sys.stdin.readline().split())
v3 = list(map(int, sys.stdin.readline().split()))
v4 = 0
for v5, v6 in enumerate(v3):
    v4 += v6
    if v4 > v2:
        print(v5 + 1)
        break
else:
    print(v1 + 1)
