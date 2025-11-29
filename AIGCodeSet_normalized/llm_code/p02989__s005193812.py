import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
v1 = float('inf')
v2 = 10 ** 9 + 7
v3 = v1
v4 = 0
v5 = 0
v6 = 1
v7 = int(input())
v8 = list(map(int, input().split()))
v8.sort()
v5 = 0
for v9 in range(v7 // 2):
    if v8[v9] == v8[v7 // 2 + v9]:
        v5 += 1
print(v5)
