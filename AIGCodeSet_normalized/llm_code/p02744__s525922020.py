v1 = int(input())
v2 = []

def f1(a1, a2):
    if len(a1) == v1:
        v2.append(a1)
    else:
        for v1 in range(a2):
            v2 = a1.copy()
            v2.append(v1)
            f1(v2, max(a2, v1))
        v2 = a1.copy()
        v2.append(a2)
        f1(v2, a2 + 1)
f1([0], 0)
v3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for v4 in v2:
    for v5 in v4:
        print(v3[v5], end='')
    print()
