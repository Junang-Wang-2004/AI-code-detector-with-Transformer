v1 = enumerate
v2, v3 = open(0)
v2 = int(v2)
v4 = [0] + [-9000000000.0] * v2
for v5, (v3, v6) in v1(sorted(((int(v3), v6) for v6, v3 in v1(v3.split())))[::-1]):
    v4 = [max(t + v3 * abs(~v6 - v5 + k + v2), v4[k - 1] + v3 * abs(~v6 + k) if k else 0) for v7, v8 in v1(v4)]
print(max(v4))
