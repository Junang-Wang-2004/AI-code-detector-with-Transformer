v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 0
for v4 in range(100):
    for v5 in range(v1):
        if v2[v5] % 2 ** v4 == 0:
            v3 = v4
        else:
            break
    else:
        v3 += 1
if v3 == 0:
    print(0)
else:
    print(v3 - 1)
