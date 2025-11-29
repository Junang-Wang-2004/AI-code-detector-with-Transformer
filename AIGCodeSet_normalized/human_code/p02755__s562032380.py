v1, v2 = map(int, input().split())
v3 = -1
for v4 in range(1, 1251):
    if v1 == int(v4 * 0.08) and v2 == int(v4 * 0.1):
        v3 = v4
        break
print(v3)
