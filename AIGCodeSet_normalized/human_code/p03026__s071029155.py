import sys
v1 = sys.stdin
v2 = lambda: int(rs())
v3 = lambda: list(map(int, v1.readline().split()))
v4 = lambda: v1.readline().rstrip()
v5 = v2()
v6 = [set() for v7 in range(v5 + 1)]
for v7 in range(v5 - 1):
    v8, v9 = v3()
    v6[v8].add(v9)
    v6[v9].add(v8)
v10 = v3()
v10.sort(reverse=True)
v11 = sum(v10[1:])
v12 = [len(x) for v13 in v6]
v14 = [i for v15, v13 in enumerate(v12) if v13 == 1]
v16 = [0] * (v5 + 1)
while v14:
    v17 = v14.pop()
    if not v14:
        v16[v17] = v10.pop()
        break
    v18 = v6[v17].pop()
    v6[v18].remove(v17)
    v12[v18] -= 1
    if v12[v18] == 1:
        v14.append(v18)
    v16[v17] = v10.pop()
print(v11)
print(*v16[1:])
