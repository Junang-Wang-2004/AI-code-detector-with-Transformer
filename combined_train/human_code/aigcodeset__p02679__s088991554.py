import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
import sys
v1 = 1000000007

def f1(a1, a2):
    while a2 != 0:
        a1, a2 = (a2, a1 % a2)
    return a1
v2 = int(input())
v3 = [() for v4 in range(v2)]
v5 = [() for v4 in range(v2)]
v6 = {}
v7 = {}
v8 = {}
v9 = {}
v10 = [False for v11 in range(v2)]
v12 = 0
v13 = [False for v11 in range(v2)]
for v4 in range(v2):
    v14, v15 = map(int, input().split())
    if v14 == 0 and v15 == 0:
        v12 += 1
        v10[v4] = True
        v13[v4] = True
    else:
        if v14 == 0:
            v3[v4] = (0, 1)
            v5[v4] = (1, 0)
        elif v15 == 0:
            v3[v4] = (1, 0)
            v5[v4] = (0, 1)
        else:
            v16 = False
            if v14 * v15 < 0:
                v16 = True
            v17 = f1(abs(v14), abs(v15))
            v14 = abs(v14) // v17
            v15 = abs(v15) // v17
            if v16:
                v3[v4] = (-v14, v15)
                v5[v4] = (v15, v14)
            else:
                v3[v4] = (v14, v15)
                v5[v4] = (-v15, v14)
        v6[v3[v4]] = v6.get(v3[v4], 0) + 1
        v7[v5[v4]] = v7.get(v5[v4], 0) + 1
        if v3[v4] not in v8:
            v8[v3[v4]] = v4
        if v5[v4] not in v9:
            v9[v5[v4]] = v4
v18 = 1
for v4 in range(v2):
    if not v13[v4] and (not v10[v8[v3[v4]]]):
        if v3[v4] not in v7:
            v18 *= pow(2, v6[v3[v4]], v1)
            v18 %= v1
            v10[v8[v3[v4]]] = True
        else:
            v19 = v6[v3[v4]]
            v20 = v7[v3[v4]]
            v18 *= (1 * pow(2, v19, v1) + 1 * pow(2, v20, v1) - 1) % v1
            v18 %= v1
            v10[v8[v3[v4]]] = True
            v10[v9[v3[v4]]] = True
print((v18 - 1 + v12) % v1)
