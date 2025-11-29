v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4 = 1
for v5 in range(1, v1 - v2 + 2):
    v4 *= v5
    v4 %= v3
for v5 in range(1, v2):
    v4 *= v5
    v4 %= v3
v6 = v1 - v2 + 1
print(v6)
for v5 in range(2, v2 + 1):
    if v1 - v2 + 1 < v5:
        print(0)
        continue
    v6 = v6 * (v1 - v2 - v5 + 2) * pow(v5, v3 - 2, v3) * pow(v5 - 1, v3 - 2, v3)
    v6 %= v3
    print(v6)
