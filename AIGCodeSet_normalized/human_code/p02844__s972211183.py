v1 = int(input())
v2 = input()
v3 = [0]
for v4 in v2:
    v3.append(v3[-1] | 1 << int(v4))
v5 = [0]
for v4 in v2[::-1]:
    v5.append(v5[-1] | 1 << int(v4))
v5.reverse()
v6 = [set() for v7 in range(10)]
for v4, v8, v9 in zip(v2, v3, v5[1:]):
    v4 = int(v4)
    for v10 in range(10):
        if v8 & 1 << v10 == 0:
            continue
        for v11 in range(10):
            if v9 & 1 << v11 == 0:
                continue
            v6[v4].add(10 * v10 + v11)
print(sum((len(m) for v12 in v6)))
