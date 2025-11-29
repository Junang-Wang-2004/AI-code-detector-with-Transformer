v1 = int(input())
v2 = []
for v3 in range(v1):
    v2.append(int(input()))
v4 = 0
v5 = 0
for v3 in range(v1):
    v6 = v2[v3]
    if v6 - v5 > 1:
        v4 = -1
        break
    elif v6 - v5 == 1:
        v4 += 1
        v5 = v6
    else:
        v4 += v6
        v5 = v6
print(str(v4))
