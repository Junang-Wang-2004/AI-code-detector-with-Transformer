v1, v2 = map(int, input().split())
v3 = ''
for v4 in range(v1):
    v5 = input()
    if v4 == 0:
        v3 = v5
    for v6 in range(v2):
        if v5[v6] < v3[v6]:
            v3 = v5 + v3
            break
        elif v5[v6] > v3[v6]:
            v3 = v3 + v5
            break
print(v3)
