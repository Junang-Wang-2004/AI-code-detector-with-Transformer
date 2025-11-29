v1 = [a for v2 in input()]
v3 = input()
v4 = {v: 0 for v5 in set(v3)}
for v5 in v3:
    if v5 in v1:
        v4[v5] = v1.index(v5)
    else:
        print(-1)
        exit()
v6 = 0
for v7 in range(1, len(v3)):
    if v4[v3[v7 - 1]] > v4[v3[v7]]:
        v6 += 1
if v4[v3[-1]] > v4[v3[-2]]:
    print(len(v1) * v6 + v1.index(v3[-1]) + 1)
else:
    print(len(v1) * (v6 - 1) + v1.index(v3[-1]) + 1)
