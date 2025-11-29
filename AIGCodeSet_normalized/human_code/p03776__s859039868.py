from scipy.misc import comb
v1, v2, v3, *v4 = map(int, open(0).read().split())
v5 = {}
for v6 in v4:
    v5[v6] = v5.get(v6, 0) + 1
v7 = sorted(v5.items(), key=lambda x: x[0])[::-1]
if v7[0][1] > v2:
    print(v7[0][0])
    print(int(sum((comb(v7[0][1], i, exact=1) for v8 in range(v2, v3 + 1)))))
else:
    v9 = 0
    v10 = v2
    for v11, v6 in v7:
        if v6 < v10:
            v9 += v11 * v6
            v10 -= v6
        else:
            print((v9 + v11 * v10) / v2)
            print(int(comb(v6, v10, exact=1)))
            break
