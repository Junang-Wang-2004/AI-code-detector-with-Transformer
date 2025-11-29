v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5 = int(input())
    v3.append(v5)
v6 = [1, 1]
for v7 in range(10 ** 5):
    v8 = (v6[-1] + v6[-2]) % (10 ** 9 + 7)
    v6.append(v8)
v3.insert(0, 0)
v3.append(v1)
v9 = 1
if v2 >= 2:
    for v4 in range(v2 + 1):
        if v4 == 0:
            v9 = v9 * v6[v3[1] - v3[0] - 1]
            v9 = v9 % (10 ** 9 + 7)
        elif v4 == v2:
            v9 = v9 * v6[v3[v2 + 1] - v3[v2] - 1]
            v9 = v9 % (10 ** 9 + 7)
        elif v4 != 0 and v4 != v2:
            if v3[v4 + 1] - v3[v4] == 1:
                v9 = 0
                break
            else:
                v9 = v9 * v6[v3[v4 + 1] - v3[v4] - 2]
                v9 = v9 % (10 ** 9 + 7)
    print(v9)
if v2 == 0:
    print(v6[v1])
if v2 == 1:
    print(v6[v3[1] - 1] * v6[v1 - v3[1] - 1] % (10 ** 9 + 7))
