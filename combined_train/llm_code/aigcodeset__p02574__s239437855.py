def f1(a1, a2):
    if a2 == 0:
        return a1
    else:
        return f1(a2, a1 % a2)

def f2(a1):
    v1 = a1[0]
    for v2 in a1:
        v1 = f1(v1, v2)
    return v1

def f3(a1, a2):
    return a1 * a2 // f1(a1, a2)

def f4(a1):
    v1 = a1[0]
    for v2 in a1:
        v1 = f3(v1, v2)
    return v1
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1
for v4 in range(v1):
    v3 *= v2[v4]
if v3 == f4(v2):
    print('pairwise coprime')
elif f2(v2) == 1:
    print('setwise coprime')
else:
    print('not coprime')
