v1 = int(input())
v2 = 0
if v1 == 1:
    v3 = 1
else:
    for v4 in range(1, v1 + 1):
        v2 += v4
        if v1 - v2 <= v4 + 1:
            v3 = v4 + 1
            break
print(v3)
