import copy
v1 = list(input())
v2 = int(input())

def f1(a1, a2):
    v1 = ''
    v2 = 0
    for v3 in a1:
        if v1 != v3:
            v1 = v3
        else:
            v2 += 1
            v1 = ''
    return v2

def f2(a1, a2):
    v1 = ''
    v2 = copy.deepcopy(a1)
    for v3 in range(0, len(a1) - 1):
        if a1[0] == a1[len(a1) - 1]:
            a1.append(a1[0])
            a1.pop(0)
        else:
            break
    return f1(a1, a2) * (a2 - 1) + f1(v2, a2)

def f3(a1, a2):
    v1 = copy.deepcopy(a1)
    a1.extend(a1)
    return f1(a1, a2) * int(a2 / 2) + f1(v1, a2) * (a2 % 2)
v3 = 1
v4 = v1[0]
for v5 in v1:
    if v4 != v5:
        v3 = 0
        break
    v4 = v5
if v3 == 0 and v1[0] != v1[len(v1) - 1]:
    v6 = f1(v1, v2) * v2
elif v3 == 0:
    v6 = f2(v1, v2)
else:
    v6 = f3(v1, v2)
print(v6)
