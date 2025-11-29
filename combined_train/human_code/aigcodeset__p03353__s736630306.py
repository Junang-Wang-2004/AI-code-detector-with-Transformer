import sys
import itertools

def f1(a1):
    v1 = a1.pop(0)
    v2 = int(a1.pop(0))
    v3 = 0
    v4 = []
    v5 = []
    while v2 > 0:
        v6 = 0
        v7 = 'z'
        for v8, v9 in enumerate(v1):
            if v8 in v4:
                continue
            if v7 > v9:
                v7 = v9
                v6 = v8
            elif v7 == v9:
                v10 = len(v1[v8:])
                if v1[v6:v6 + v10] > v1[v8:]:
                    v7 = v9
                    v6 = v8
                elif v1[v6:v6 + v10] == v1[v8:]:
                    v4.append(v8)
        v4.append(v6)
        v5 = v1[v6:]
        if len(v5) >= v2:
            print(v5[:v2])
            sys.exit(0)
        else:
            v2 -= len(v5)
    sys.exit(1)
v1 = [x.strip() for v2 in sys.stdin.readlines()]
f1(v1)
