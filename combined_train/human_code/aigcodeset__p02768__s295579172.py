v1, v2, v3 = map(int, input().split())
v4 = 10 ** 9 + 7

def f1(a1, a2):
    v1 = [a1]
    while 2 ** len(v1) < a2 + 1:
        v1.append(v1[-1] ** 2 % v4)
    v2 = bin(a2)
    v3 = 1
    for v4 in range(len(v2) - 2):
        if int(v2[-v4 - 1]) == 1:
            v3 = v3 * v1[v4] % v4
    return v3
v5 = 2 * 10 ** 5 + 10
v6 = [1, 1]
v7 = [1, 1]
v8 = [0, 1]
for v9 in range(2, v5 + 1):
    v6.append(v6[-1] * v9 % v4)
    v8.append(-v8[v4 % v9] * (v4 // v9) % v4)
    v7.append(v7[-1] * v8[-1] % v4)
v10 = 1
for v9 in range(v2):
    v10 = v10 * (v1 - v9) % v4
v10 = v10 * v7[v2] % v4
v11 = 1
for v9 in range(v3):
    v11 = v11 * (v1 - v9) % v4
v11 = v11 * v7[v3] % v4
v12 = f1(2, v1) - 1
v12 = (v12 - v10) % v4
v12 = (v12 - v11) % v4
print(v12)
