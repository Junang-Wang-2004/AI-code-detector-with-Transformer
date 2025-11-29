v1 = int(input())
v2 = 0
for v3 in range(1, int(v1 ** 0.5) + 2):
    if (v1 - v3) % v3 != 0:
        continue
    else:
        v4 = (v1 - v3) // v3
        if v4 <= v3:
            break
        else:
            v2 += v4
print(v2)
