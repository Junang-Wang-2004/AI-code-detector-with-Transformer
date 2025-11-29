v1, v2 = map(int, input().split())
v3 = 0
for v4 in range(v1, v2 + 1):
    if str(v4) == str(v4)[::-1]:
        v3 += 1
print(v3)
