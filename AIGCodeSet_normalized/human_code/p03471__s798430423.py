import sys
v1, v2 = map(int, input().split())
for v3 in range(v1 + 1):
    if v3 * 10000 > v2:
        break
    for v4 in range(v1 + 1 - v3):
        v5 = v1 - (v3 + v4)
        if v3 * 10000 + v4 * 5000 + v5 * 1000 == v2:
            print(v3, v4, v5)
            sys.exit()
print(-1, -1, -1)
