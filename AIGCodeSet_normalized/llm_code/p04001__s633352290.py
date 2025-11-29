v1 = input()
v2 = len(v1)
v3 = 0
for v4 in range(1 << v2 - 1):
    v5 = v1[0]
    for v6 in range(v2 - 1):
        if v4 & 1 << v6:
            v5 += '+'
        v5 += v1[v6 + 1]
    v3 += sum(map(int, v5.split('+')))
print(v3)
