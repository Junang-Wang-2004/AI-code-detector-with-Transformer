import sys
v1 = int(sys.stdin.readline().rstrip())
v2 = sys.stdin.readline().rstrip()
v3 = int(sys.stdin.readline().rstrip())
v4 = [{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} for v5 in range(v1 + 1)]

def f1(a1, a2):
    for v1 in a1.keys():
        a1[v1] += a2[v1]
    return a1

def f2(a1, a2):
    for v1 in a1.keys():
        a1[v1] -= a2[v1]
    return a1

def f3(a1):
    return 26 - list(a1.values()).count(0)

def f4(a1):
    v1 = f2(f6(a1), f6(a1 - 1))
    for v2, v3 in v1.items():
        if v3 == 1:
            return v2
for v6 in range(v1):
    v7 = v6 + 1
    while v7 <= v1:
        v4[v7][v2[v6]] += 1
        v7 += v7 & -v7

def f5(a1, a2, a3):
    global BIT, N
    while a1 <= v1:
        v4[a1][a3] -= 1
        v4[a1][a2] += 1
        a1 += a1 & -a1

def f6(a1):
    global BIT, N
    v1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    while a1 > 0:
        v1 = f1(v1, v4[a1])
        a1 -= a1 & -a1
    return v1
for v5 in range(v3):
    v8, v9, v10 = sys.stdin.readline().rstrip().split()
    if v8 == '1':
        v9 = int(v9)
        v11 = f4(v9)
        f5(v9, v10, v11)
    else:
        v9 = int(v9)
        v10 = int(v10)
        print(f3(f2(f6(v10), f6(v9 - 1))))
