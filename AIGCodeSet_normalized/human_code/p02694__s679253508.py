def f1(a1):
    v1 = 100
    v2 = v1
    v3 = 0
    while v2 < a1:
        v2 += int(0.01 * v2)
        v3 += 1
    return v3

def f2():
    return int(input())
v1 = f2()
print(f1(v1))
