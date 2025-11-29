v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4, v5 = (1, [0] * (2 * 10 ** 5 + 1))
v2.append(0)
v5[v2[0]] += 1
for v6 in range(1, v1):
    if v2[v6] == v2[v6 - 1]:
        v4 = v4 * 2 % (10 ** 9 + 7)
    else:
        v5[v2[v6]] += v4
        v4 = v5[v2[v6]]
print(v4)
