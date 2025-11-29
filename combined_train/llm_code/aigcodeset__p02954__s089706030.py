v1 = input()
v2 = len(v1)

def f1(a1):
    v1 = a1[0]
    v2 = 1
    v3 = ''
    for v4 in range(1, len(a1)):
        if v1 == a1[v4]:
            v2 += 1
        else:
            v3 += v1 + str(v2)
            v1 = a1[v4]
            v2 = 1
    v3 += v1 + str(v2)
    return v3
v3 = list(f1(v1))
v4 = [0] * v2
v5 = 0
for v6 in range(0, len(v3), 4):
    v7 = int(v3[v6 + 1])
    v8 = int(v3[v6 + 3])
    v9 = v7 // 2 + (v8 + 1) // 2
    v10 = v7 + v8 - v9
    v4[v5 + v7 - 1] = v10
    v4[v5 + v7] = v9
    v5 += v7 + v8
print(*v4)
