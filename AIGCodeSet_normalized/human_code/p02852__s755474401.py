import sys
sys.setrecursionlimit(10 ** 9)
v1, v2 = map(int, input().split())
v3 = input()
v4 = float('inf')
v5 = [v4 for v6 in range(v1 + 1)]
v5[v1] = 0
v7 = v1
for v8 in range(v1 - 1, -1, -1):
    while v7 - v8 > v2 or v5[v7] == v4:
        v7 -= 1
    if v7 <= v8:
        print(-1)
        exit()
    if v3[v8] == '0':
        v5[v8] = v5[v7] + 1
        v9 = v5[v8]
v10 = []
v11 = 0
for v8 in range(v1 + 1):
    if v5[v8] != v4 and v5[v8] != v9:
        v9 = v5[v8]
        v10.append(v11)
        v11 = 1
    else:
        v11 += 1
print(*v10)
