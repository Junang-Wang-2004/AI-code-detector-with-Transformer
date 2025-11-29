v1, v2 = map(int, input().split())
v3 = 10 ** 9 + 7
v4 = [int(x) for v5 in input().split()]
v6 = [int(v5) for v5 in input().split()]
v7 = [(v4[i + 1] - v4[i]) * (v1 - i - 1) * (i + 1) % v3 for v8 in range(v1 - 1)]
v9 = [(v6[j + 1] - v6[j]) * (v2 - j - 1) * (j + 1) % v3 for v10 in range(v2 - 1)]
print(sum(v7) * sum(v9) % v3)
