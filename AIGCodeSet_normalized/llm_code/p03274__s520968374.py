v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [sum([abs(v3[j]) if j == i else abs(v3[j] - v3[j - 1]) for v5 in range(i, i + v2)]) for v6 in range(0, v1 - v2)] + [sum([abs(v3[v5]) if v5 == v6 else abs(v3[v5 + 1] - v3[v5]) for v5 in range(v6, v6 - v2, -1)]) for v6 in range(v2, v1)]
print(min(v4))
