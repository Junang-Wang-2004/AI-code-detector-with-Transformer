v1, v2 = map(int, input().split())
v3 = [int(i) for v4 in input().split()]
v5 = [True for v4 in range(v1)]
for v4 in range(v2):
    v6, v7 = map(int, input().split())
    if v3[v6 - 1] > v3[v7 - 1]:
        v5[v7 - 1] = False
    elif v3[v6 - 1] < v3[v7 - 1]:
        v5[v6 - 1] = False
    else:
        v5[v6 - 1] = False
        v5[v7 - 1] = False
v8 = 0
for v4 in range(v1):
    if v5[v4] == True:
        v8 += 1
print(v8)
