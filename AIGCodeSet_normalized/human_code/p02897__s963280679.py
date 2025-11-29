v1 = int(input())
v2 = 0.0
for v3 in range(1, v1 + 1):
    if v3 % 2 != 0:
        v2 += 1
print(v2 / v1)
