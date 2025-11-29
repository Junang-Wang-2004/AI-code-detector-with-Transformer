v1, v2 = map(int, input().split())
v3 = -1
for v4 in range(1300):
    if int(v4 * 2 / 25) == v1 and int(v4 / 10) == v2:
        v3 = v4
        break
print(v3)
