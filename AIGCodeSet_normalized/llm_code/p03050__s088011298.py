v1 = int(input())
v2 = 0
for v3 in range(1, int(v1 ** 0.5) + 1):
    if v1 % v3 == 0:
        v2 += v1 // v3
        if v3 * v3 != v1:
            v2 += v1 // v3 - 1
print(v2)
