def f1(a1):
    return a1 == a1[::-1]

def f2(a1):
    if f1(a1):
        return 0
    v1 = float('inf')
    for v2 in range(len(a1)):
        if f1(a1[:v2] + a1[v2 + 1:]):
            v1 = min(v1, 1 + f2(a1[:v2] + a1[v2 + 1:]))
    return v1 if v1 != float('inf') else -1
