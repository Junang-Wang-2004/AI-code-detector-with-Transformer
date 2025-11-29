def f1(a1):
    v1 = str(a1)
    for v2 in range(len(v1) - 1):
        if abs(int(v1[v2]) - int(v1[v2 + 1])) > 1:
            return False
    return True

def f2(a1):
    v1 = 0
    v2 = 1
    while v1 < a1:
        if f1(v2):
            v1 += 1
        v2 += 1
    return v2 - 1
v1 = int(input())
print(f2(v1))
