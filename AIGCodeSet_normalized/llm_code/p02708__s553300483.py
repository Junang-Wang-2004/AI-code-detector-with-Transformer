v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7

def f1(a1, a2):
    if a1 == 0:
        return 0
    v1 = (0 + a2 - 1) * a2 // 2 % v3
    v2 = (2 * a1 - a2 + 1) * a2 // 2 % v3
    return (v2 - v1 + 1) % v3
v4 = [f1(v1, m) for v5 in range(1, v1 + 2)]
v6 = sum(v4[v2 - 1:]) % v3
print(v6)
