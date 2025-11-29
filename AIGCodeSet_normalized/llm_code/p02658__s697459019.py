v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in range(v1):
    if v2[v4] == 0:
        v3 = 0
        break
    elif v3 > 10 ** 18 // v2[v4]:
        v3 = -1
        break
    else:
        v3 = v3 * v2[v4]
print(v3)
