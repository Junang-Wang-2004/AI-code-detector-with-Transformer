v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v1, v2 + 1):
    v5 = ''.join(list(reversed(str(v4))))
    if str(v4) == v5:
        v3 += 1
print(v3)
