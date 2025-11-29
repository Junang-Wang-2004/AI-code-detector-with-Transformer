def f1():
    v1 = int(input())
    v2 = list(input())
    v3 = 0
    v4 = 0
    for v5 in v2:
        if v5 == '(':
            v3 += 1
        elif v5 == ')':
            v3 -= 1
        if v3 < 0:
            v4 += 1
            v3 += 1
    v6 = []
    for v5 in range(v4):
        v6.append('(')
    v2 = v6 + v2
    v7 = 0
    v8 = 0
    for v5 in v2:
        if v5 == '(':
            v7 += 1
        elif v5 == ')':
            v8 += 1
    v6 = []
    for v5 in range(v7 - v8):
        v6.append(')')
    v2 = v2 + v6
    for v5 in v2:
        print(v5, end='')
    print()
f1()
