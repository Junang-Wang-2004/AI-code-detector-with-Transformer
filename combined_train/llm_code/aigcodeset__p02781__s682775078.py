def f1(a1):
    return a1 * (a1 - 1) / 2

def f2(a1):
    return a1 * (a1 - 1) * (a1 - 2) / 2 / 3

def f3(a1):
    while a1[0] == '0' and len(a1) > 0:
        a1 = a1[1:]
    v2 = len(a1)
    if v2 == 1 or v2 == 0:
        v3 = int(a1[0])
    elif v2 > 1:
        v3 = int(a1[0]) + 9 * (v2 - 1)
    return v3

def f4(a1):
    while a1[0] == '0' and len(a1) > 0:
        a1 = a1[1:]
    v2 = len(a1)
    if v2 == 1 or v2 == 0:
        v3 = 0
    elif v2 == 2:
        v3 = (int(a1[0]) - 1) * 9 + int(a1[1])
    else:
        v3 = f3(a1[1:]) + (int(a1[0]) - 1) * (v2 - 1) * 9 + 9 * 9 * f1(v2 - 1)
    return v3

def f5(a1):
    v1 = len(a1)
    if v1 == 1 or v1 == 2:
        v2 = 0
    elif v1 == 3:
        v2 = (int(a1[0]) - 1) * 9 * 9 + int(a1[1]) * int(a1[2])
    else:
        v2 = f4(a1[1:]) + (int(a1[0]) - 1) * f1(v1 - 1) * 9 * 9 + f2(v1 - 1) * 9 * 9 * 9
    return v2
v1 = input()
v2 = input()
if v2 == '1':
    v3 = f3(v1)
elif v2 == '2':
    v3 = f4(v1)
elif v2 == '3':
    v3 = f5(v1)
print(int(v3))
