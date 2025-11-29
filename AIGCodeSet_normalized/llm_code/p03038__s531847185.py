import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v5 = []
v6 = []
for v4 in range(v2):
    v7, v8 = map(int, input().split())
    v5.append(v7)
    v6.append(v8)
v9 = sum(v3)
for v4 in range(v2):
    for v10 in range(v5[v4]):
        if len(v3) == 0:
            break
        v3.sort()
        if v6[v4] > v3[0]:
            v9 += v6[v4] - v3[0]
            v3.pop(0)
        else:
            break
print(v9)
