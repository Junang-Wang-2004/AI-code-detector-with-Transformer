v1 = input()
v2 = int(input())
v3 = []
v4 = 0
v5 = 0
for v6 in range(len(v1)):
    if v6 == 0:
        v3.append(v1[v6])
    elif v1[v6] == v3[-1]:
        v5 += 1
    else:
        if v5 != 0:
            v4 += (v5 + 1) // 2
            v5 = 0
        v3.append(v1[v6])
if v5 != 0:
    v4 += (v5 + 1) // 2
v4 *= v2
if len(v3) == 1:
    v4 = len(v1) * v2
elif v3[0] == v3[-1]:
    v4 += (v5 + 1) // 2 * (v2 - 1)
print(v4)
