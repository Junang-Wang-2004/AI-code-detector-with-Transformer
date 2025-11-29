v1, v2 = map(int, input().split())
v3 = [input() for v4 in range(v1)]
v5 = []
for v6 in range(2 * v1):
    if v6 % 2 == 0:
        v5.append(v3[v6 // 2])
    else:
        v5.append(''.join((c for v7 in v3[v6 // 2] if v7 == '.')))
print('\n'.join(v5))
