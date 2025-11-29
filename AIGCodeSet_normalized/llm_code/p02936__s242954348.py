class C1:

    def __init__(self, a1, a2):
        self.num = a1
        self.val = a2
        self.children = []
        self.progeny_num = []

def f1(a1):
    a1.progeny_num = [a1.num]
    if len(a1.children) == 0:
        return
    for v1 in a1.children:
        f1(v1)
        a1.progeny_num.extend(v1.progeny_num)
    return
[v1, v2] = [int(i) for v3 in input().split()]
v4 = []
for v5 in range(v1 - 1):
    [v6, v7] = [int(v3) for v3 in input().split()]
    v4.append((v6, v7))
v8 = []
for v9 in range(v2):
    [v10, v11] = [int(v3) for v3 in input().split()]
    v8.append((v10, v11))
v12 = {}
for v6, v7 in v4:
    v13 = v12[v6] if v6 in v12 else C1(v6, 0)
    v14 = v12[v7] if v7 in v12 else C1(v7, 0)
    v13.children.append(v14)
    if v6 not in v12:
        v12[v6] = v13
    if v7 not in v12:
        v12[v7] = v14
for v3 in range(1, v1 + 1):
    f1(v12[v3])
for v10, v11 in v8:
    for v15 in v12[v10].progeny_num:
        v12[v15].val += v11
v16 = ''
for v17 in v12.values():
    v16 += str(v17.val) + ' '
print(v16)
