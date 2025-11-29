v1 = int(input())
v2 = [input().split() for v3 in range(v1)]
for v3 in range(0, len(v2)):
    v2[v3][0] = float(v2[v3][0])
v4 = 0
for v3 in range(0, len(v2)):
    if v2[v3][1] == 'JPY':
        v4 += v2[v3][0]
    else:
        v4 += v2[v3][0] * 380000
print(v4)
