v1 = int(input())
v2 = 0.0
v3 = 0.0
for v4 in range(v1):
    v5 = v4 + 1
    if v5 % 2 == 0:
        v3 = v3 + 1
    else:
        v2 = v2 + 1
v6 = v2 / (v2 + v3)
print(v6)
