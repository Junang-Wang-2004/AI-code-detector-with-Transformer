import sys
input = sys.stdin.readline
v1 = int(input())
v2 = [set() for v3 in range(v1)]
v4 = [[int(v3) - 1 for v3 in input().split()] for v5 in range(v1 - 1)]
v6 = ['' for v3 in range(v1)]
v7 = [int(v3) for v3 in input().split()]
v7.sort()
v8 = sum(v7[:-1])
v9 = []
for v3, v10 in v4:
    v2[v3].add(v10)
    v2[v10].add(v3)
for v3, v11 in enumerate(v2):
    if len(list(v11)) == 1:
        v9.append(v3)
for v5 in range(v1 - 1):
    v3 = v9.pop(0)
    v10 = list(v2[v3])[0]
    v6[v3] = str(v7.pop(0))
    v2[v10].remove(v3)
    if len(list(v2[v10])) == 1:
        v9.append(v10)
v3 = v9.pop(0)
v6[v3] = str(v7.pop(0))
print(v8)
print(' '.join(v6))
