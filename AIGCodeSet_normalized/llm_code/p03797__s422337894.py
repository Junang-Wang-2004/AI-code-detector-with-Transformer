v1, v2 = [int(i) for v3 in input().split()]

def f1(a1, a2):
    if a1 >= a2 // 2:
        v1 = a2 // 2
        a2 -= v1 * 2
        a1 -= v1
        v1 += min(a1, a2 // 2)
    else:
        v1 = a1
    return v1
print(f1(v1, v2))
