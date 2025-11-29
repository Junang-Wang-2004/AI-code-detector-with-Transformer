v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = []
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    if v3[v6 - 1] < v3[v7 - 1]:
        v4.append(v6)
    elif v3[v6 - 1] > v3[v7 - 1]:
        v4.append(v7)
    else:
        v4.append(v6)
        v4.append(v7)
print(v1 - len(list(set(v4))))
