v1 = int(input())
v2 = int(input())

def f1(a1, a2):
    v1 = 0
    for v2 in range(1, a1 + 1):
        if v2 <= a2:
            v1 += 1900
        else:
            v1 += 100
    return v1
print(f1(v1, v2))
