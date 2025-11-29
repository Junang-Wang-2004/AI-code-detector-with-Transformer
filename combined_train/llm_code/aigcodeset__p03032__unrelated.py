v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = 0
v5 = 0
v6 = 0
v7 = v1 - 1
v8 = []
while v2 > 0:
    if v6 <= v7 and (v3[v6] > 0 or v6 == v7):
        v8.append(v3[v6])
        v6 += 1
    elif v6 <= v7:
        v8.append(v3[v7])
        v7 -= 1
    elif v8 and v8[0] > 0:
        v6 -= 1
        v3.insert(v6, v8.pop(0))
    elif v8:
        v7 += 1
        v3.insert(v7, v8.pop())
    else:
        break
    v5 = sum(v8)
    v4 = max(v4, v5)
    v2 -= 1
print(v4)
