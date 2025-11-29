v1, v2 = map(int, input().split())
v3 = 0
for v1 in range(v1):
    v4, v5 = map(int, input().split())
    v6 = (v4 ** 2 + v5 ** 2) ** 0.5
    if v6 <= v2:
        v3 += 1
print(v3)
