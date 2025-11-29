import numpy as np
v1 = int(input())
v2 = [0] * (v1 + 1)

def f1(a1):
    v1 = []
    v2 = a1
    for v3 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v2 % v3 == 0:
            v4 = 0
            while v2 % v3 == 0:
                v4 += 1
                v2 //= v3
            v1.append([v3, v4])
    if v2 != 1:
        v1.append([v2, 1])
    if v1 == []:
        v1.append([a1, 1])
    return v1
for v3 in range(1, v1 + 1):
    v4 = f1(v3)
    for v5, v6 in v4:
        v2[v5] += v6
v7 = np.array(v2)
v8 = v7[v7 >= 2]
v9 = v7[v7 >= 4]
v10 = v7[v7 >= 14]
v11 = v7[v7 >= 24]
v12 = v7[v7 >= 74]
v13 = len(v12)
v14 = len(v11) * (len(v8) - len(v11)) + len(v11) * (len(v11) - 1) // 2
v15 = len(v10) * (len(v9) - len(v10)) + len(v10) * (len(v10) - 1) // 2
v16 = len(v9) * (len(v9) - 1) * (len(v8) - len(v9)) // 2 + len(v9) * (len(v9) - 1) * (len(v9) - 2) // 6
print(v13 + v14 + v15 + v16 + 1)
