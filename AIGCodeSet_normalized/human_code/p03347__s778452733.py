v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = 0
if v2[0] != 0:
    v4 = -1
elif v1 == 1:
    v4 = 0
else:
    v5 = v2[1:]
    for v6, v7 in enumerate(v5):
        if v7 <= 1:
            v4 += v7
        else:
            v8 = v7 - v2[v6]
            if v8 == 1:
                v4 += 1
            elif v8 <= 0:
                v4 += v7
            else:
                v4 = -1
                break
print(v4)
