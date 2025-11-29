v1, v2 = map(int, input().split())

def f1(a1, a2=10 ** 9 + 7):
    return pow(a1, a2 - 2, a2)

def f2(a1, a2, a3=10 ** 9 + 7):
    a2 = min(a2, a1 - a2)
    v2 = 1
    for v3 in range(a2):
        v2 = v2 * (a1 - v3) * f1(v3 + 1, a3) % a3
    return v2
v3 = 10 ** 9 + 7
v4 = [1]
for v5 in range(v1):
    v4 += [v4[-1] * (v5 + 1) % v3]

def f3(a1, a2):
    return v4[a1] * pow(v4[a2], v3 - 2, v3) * pow(v4[a1 - a2], v3 - 2, v3) % v3
v6 = list(map(int, input().split()))
v6.sort()
v7 = v6[::-1]
v8 = 0
for v5 in range(v2 - 1, v1):
    v8 += (v6[v5] - v7[v5]) * f3(v5, v2 - 1) % (10 ** 9 + 7)
print(v8 % (10 ** 9 + 7))
