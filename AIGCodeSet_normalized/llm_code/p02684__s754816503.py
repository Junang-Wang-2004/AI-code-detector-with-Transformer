v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = [1]
v5 = 1
v6 = True
for v7 in range(v2):
    if v3[v5 - 1] not in v4:
        v5 = v3[v5 - 1]
        v4.append(v5)
    else:
        v8 = len(v4) - v4.index(v3[v5 - 1])
        print(v4[v4.index(v3[v5 - 1]) + (v2 - v7) % v8])
        v6 = False
        break
if v6:
    print(v5)
