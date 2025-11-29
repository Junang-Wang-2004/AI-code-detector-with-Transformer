import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = sum(v2)
v5 = sum(v3)
v6 = v5 - v4
if v6 < 0:
    print('No')
    exit()
v7 = 0
v8 = 0
for v9 in range(v1):
    v10 = v3[v9] - v2[v9]
    if v10 > 0:
        v7 += v10 // 2
        v8 += v10 % 2
    elif v10 < 0:
        v8 -= v10
v11 = v6 - v7
v12 = v6 - v8
if v11 < 0 or v12 < 0:
    print('No')
    exit()
if v12 / v11 == 2:
    print('Yes')
else:
    print('No')
