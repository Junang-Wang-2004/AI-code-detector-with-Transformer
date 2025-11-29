import sys
v1 = sys.stdin.buffer.read
v2 = sys.stdin.buffer.readline
v3 = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)
v4, v5, *v6 = map(int, v1().split())
v7 = 0
v8 = 0
for v9 in v6:
    if v6[v9] % 2 == 1:
        v7 += 1
    else:
        v8 += 1
v10 = 2 ** max(0, v7 - 1) * 2 ** v8
if v5 == 1 and v7 == 0:
    v10 = 0
print(v10)
