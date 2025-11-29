def f1(a1, a2):
    if 0 <= a2 <= a1:
        v1 = 1
        for v2 in range(a2):
            v1 *= a1 - v2
            v1 //= v2 + 1
        return v1
    else:
        return 0
v1 = int(input())
v2 = int(input())
v3 = 0
for v4 in range(1, v1 + 1):
    v5 = str(v4)
    if v5.count('0') == len(v5) - v2:
        v3 += 1
print(v3)
