def f1(a1, a2, a3):
    v1 = []
    v2 = float('inf')
    for v3 in itertools.product(range(1, a2 + 1), repeat=a1):
        if f2(v3, a3):
            v4 = len(v3)
            if v4 < v2:
                v1 = v3
                v2 = v4
    return v1

def f2(a1, a2):
    v1 = 0
    v2 = 0
    for v3 in a1:
        if a2[v1] == 1:
            return False
        v1 += v3
        if v1 > n:
            return False
        v2 += 1
    return True
v1 = 19
v2 = 3
v3 = '0001000100'
print(f1(v1, v2, v3))
