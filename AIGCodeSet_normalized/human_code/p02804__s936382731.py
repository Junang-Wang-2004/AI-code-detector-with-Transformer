v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
sum = 0

def f1(a1, a2, a3):
    if a2 < 0 or a2 > a1:
        return 0
    a2 = min(a2, a1 - a2)
    return g1[a1] * g2[a2] * g2[a1 - a2] % a3
v4 = 10 ** 9 + 7
v5 = 10 ** 5
v6 = [1, 1]
v7 = [1, 1]
v8 = [0, 1]
for v9 in range(2, v5 + 1):
    v6.append(v6[-1] * v9 % v4)
    v8.append(-v8[v4 % v9] * (v4 // v9) % v4)
    v7.append(v7[-1] * v8[-1] % v4)
for v9 in range(v1):
    sum += v3[v9] * f1(v9, v2 - 1, v4) - v3[v9] * f1(v1 - v9 - 1, v2 - 1, v4)
print(sum % (10 ** 9 + 7))
