import sys
input = sys.stdin.readline
v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
if v2[0] != 0:
    print(-1)
    exit()
v4 = 0
for v5 in range(1, v1):
    if v2[v5] > v2[v5 - 1]:
        v4 += v2[v5] - v2[v5 - 1]
    else:
        v4 += 1
print(v4)
