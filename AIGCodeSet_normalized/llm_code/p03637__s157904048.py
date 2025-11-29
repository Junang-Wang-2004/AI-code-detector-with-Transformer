import sys
input = sys.stdin.readline
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
v4 = 0
for v5 in range(v1):
    if v2[v5] % 4 == 0:
        v4 += 1
    elif v2[v5] % 2 == 0:
        v3 += 1
if v3 > 1:
    v6 = len(v2) - v4 * 3 - v3
if v3 == 1:
    v6 = len(v2) - v4 * 3
print('Yes' if v6 <= 0 else 'No')
