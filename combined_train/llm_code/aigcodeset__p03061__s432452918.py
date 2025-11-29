import copy

def f1(a1, a2):
    if a2 == 0:
        return a1
    return f1(a2, a1 % a2)

def f2(a1):
    v1 = 0
    for v2 in range(len(a1) - 1):
        if v2 == 0:
            v1 = f1(a1[v2], a1[v2 + 1])
        else:
            v1 = f1(v1, a1[v2 + 1])
    return v1

def f3(a1):
    v1 = copy.deepcopy(a1)
    if len(a1) == 1:
        return a1[0]
    else:
        v1.append(f1(v1.pop(), v1.pop()))
        return f3(v1)
v1 = int(input())
v2 = list(map(int, input().split()))
v2 = list(set(v2))
v3 = []
v3.append(f3(v2))
if len(v2) != 2:
    for v4 in range(len(v2)):
        v5 = copy.deepcopy(v2)
        del v5[v4]
        v3.append(f3(v5))
    print(max(v3))
elif len(v2) == 1:
    print(v2[0])
else:
    print(max(v3))
