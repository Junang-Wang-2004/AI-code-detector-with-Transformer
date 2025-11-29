v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v2.append(int(input()))
v5 = sorted(v2)
v6 = v5[-1]
v7 = v5[-2]
for v8 in v2:
    if v8 != v6:
        v3.append(str(v6))
    else:
        v3.append(str(v7))
print('\n'.join(v3))
