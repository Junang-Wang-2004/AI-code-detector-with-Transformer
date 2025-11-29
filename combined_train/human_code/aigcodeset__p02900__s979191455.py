v1 = input().split()
v2 = int(v1[0])
v3 = int(v1[1])

def f1(a1):
    v1 = []
    v2 = []
    v3 = a1
    for v4 in range(2, int(-(-a1 ** 0.5 // 1)) + 1):
        if v3 % v4 == 0:
            v5 = 0
            while v3 % v4 == 0:
                v5 += 1
                v3 //= v4
            v2.append([v4, v5])
            v1.append(v4)
    if v3 != 1:
        v2.append([v3, 1])
        v1.append(v3)
    if v2 == []:
        v2.append([a1, 1])
        v1.append(a1)
    return v1
v4 = []
v5 = []
v6 = []
v7 = 0
v4 = f1(v2)
v5 = f1(v3)
for v8 in v4:
    if v8 in v5:
        v6.append(v8)
        v7 += 1
if v2 == 1 and v3 == 1:
    print(v7)
else:
    print(v7 + 1)
