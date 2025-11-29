v1, v2 = [int(i) for v3 in input().split()]
v4 = [0 for v3 in range(v1)]
v5 = [0 for v3 in range(v1)]
v6 = [0 for v3 in range(v1)]
for v3 in range(v2):
    v7, v8 = input().split()
    if v8 == 'AC':
        if v5[int(v7) - 1] == 0:
            v5[int(v7) - 1] = 1
            v6[int(v7) - 1] = v4[int(v7) - 1]
    elif v5[int(v7) - 1] == 0:
        v4[int(v7) - 1] += 1
print(sum(v5), sum(v6))
