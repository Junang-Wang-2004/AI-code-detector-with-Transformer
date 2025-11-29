v1 = input()
v2 = len(v1)

def f1(a1, a2):
    v1 = ''
    v2 = 0
    v3 = False
    for v4 in range(len(a1) - 1):
        if a1[v4] != a2 and a1[v4 + 1] != a2:
            v1 += a1[v4]
            v3 = True
        else:
            v1 += a2
    if v3:
        v2 = v2(v1, a2)
    return v2 + 1
for v3 in v1:
    v2 = min(v2, f1(v1, v3))
print(v2)
