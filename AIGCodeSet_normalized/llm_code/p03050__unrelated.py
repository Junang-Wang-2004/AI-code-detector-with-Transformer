v1 = int(input())

def f1(a1):
    return v1 // a1 == v1 % a1
v2 = [m for v3 in range(1, int(v1 ** 0.5) + 1) if f1(v3)]
v2 += [v1 // v3 for v3 in v2 if v1 // v3 != v3]
print(sum(v2))
