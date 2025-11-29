def f1(a1, a2):
    if type(a1) is int:
        return a1 + a2
    v1 = len(set([a1, a2]))
    if a1 == None:
        v1 -= 1
    if a2 == None:
        v1 -= 1
    return v1

def f2(a1):
    for v1 in range(len(a1)):
        seg[v1 + num - 1] = a1[v1]
    for v1 in range(num - 2, -1, -1):
        seg[v1] = f1(seg[2 * v1 + 1], seg[2 * v1 + 2])

def f3(a1, a2):
    a1 += num - 1
    seg[a1] = a2
    while a1:
        a1 = (a1 - 1) // 2
        seg[a1] = f1(seg[a1 * 2 + 1], seg[a1 * 2 + 2])

def f4(a1, a2):
    if a2 <= a1:
        return ide_ele
    a1 += num - 1
    a2 += num - 2
    v3 = ide_ele
    while a2 - a1 > 1:
        if a1 & 1 == 0:
            v3 = f1(v3, seg[a1])
        if a2 & 1 == 1:
            v3 = f1(v3, seg[a2])
            a2 -= 1
        a1 = a1 // 2
        a2 = (a2 - 1) // 2
    if a1 == a2:
        v3 = f1(v3, seg[a1])
    else:
        v3 = f1(f1(v3, seg[a1]), seg[a2])
    return v3
v1 = int(input())
v2 = list(input())
v3 = None
v4 = 2 ** (v1 - 1).bit_length()
v5 = [v3] * (2 * v4 - 1)
f2(v2)
for v6 in range(int(input())):
    v7, v8, v9 = input().split()
    if v7 == '1':
        f3(int(v8) - 1, v9)
    else:
        print(f4(int(v8) - 1, int(v9) - 1))
