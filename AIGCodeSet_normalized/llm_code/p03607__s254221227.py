v1 = int(input())
v2 = [False] * 10 ** 9
v3 = 0
for v4 in range(v1):
    v5 = int(input())
    if v2[v5 - 1]:
        v3 -= 1
    else:
        v3 += 1
        v2[v5 - 1] = True
print(v3)
