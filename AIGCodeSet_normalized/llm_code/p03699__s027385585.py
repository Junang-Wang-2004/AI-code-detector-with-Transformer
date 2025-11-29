v1 = int(input())
v2 = []
for v3 in range(v1):
    v4 = int(input())
    v2.append(v4)
v5 = sum(v2)
v2.sort()
if v5 % 10 != 0:
    print(v5)
else:
    for v6 in range(v1):
        if v2[v6] % 10 != 0:
            v5 -= v2[v6]
            break
    print(v5)
