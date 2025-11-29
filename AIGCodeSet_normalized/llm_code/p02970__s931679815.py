v1, v2 = list(map(int, input().split()))
v3 = 1
v4 = 2 * v2 + 1
while v4 < v1:
    v4 = v4 * 2
    v3 += 1
print(v3)
