v1, v2 = map(int, input().split())
v3 = range(v1, v2 + 1)
v4 = 0
for v5 in v3:
    v6 = str(v5)
    v7 = ''.join(list(reversed(v6)))
    if v6 == v7:
        v4 += 1
print(v4)
