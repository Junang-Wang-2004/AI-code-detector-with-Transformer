def f1(a1):
    v1 = 0
    for v2 in a1:
        if v2 % 4 == 0:
            v1 += 1
    return v1

def f2(a1):
    v1 = 0
    for v2 in a1:
        if v2 % 2 == 0:
            v1 += 1
    return v1
v1 = int(input())
v2 = list(map(int, input().split()))

def f3(a1):
    v1 = f1(a1)
    v2 = f2(a1) - v1
    v3 = len(a1) - v1 - v2
    if v3 < v1 + 1:
        return 'Yes'
    elif v1 + 1 - v3 == 0 and v2 == 0:
        return 'Yes'
    else:
        return 'No'
print(f3(v2))
