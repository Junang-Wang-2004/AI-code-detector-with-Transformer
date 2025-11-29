v1 = int(input())
v2 = input().split()
v3 = list()
for v4 in v2:
    v3.append(int(v4))
v2 = v3

def f1(a1, a2, a3):
    if not a3:
        return False
    if len(a1) == 0:
        return True
    if 2 * a2 >= max(a1):
        return True
    v1 = min(a1)
    if 2 * a2 >= v1:
        a2 += v1
        a1.remove(v1)
        if f1(a1, a2, True):
            return True
        else:
            a2 -= v1
            a1.append(v1)
    return False
v5 = 0
for v4 in range(len(v2)):
    v6 = list(v2)
    v6.remove(v2[v4])
    if f1(v6, v2[v4], True):
        v5 += 1
print(v5)
