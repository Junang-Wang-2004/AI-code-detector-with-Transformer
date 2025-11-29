v1 = int(input())
v2 = input().split()
v3 = 0
for v4 in range(1, v1 - 1):
    if v4 == 0:
        continue
    elif v4 == int(v2[v4]):
        continue
    else:
        v3 += 1
print(v3)
