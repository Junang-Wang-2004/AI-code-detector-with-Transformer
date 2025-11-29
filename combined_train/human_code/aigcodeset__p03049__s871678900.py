import sys

def f1(a1: int, a2: 'List[str]'):
    v1 = 0
    v2 = 0
    v3 = 0
    for v4 in a2:
        if v4[0] == 'B' and v4[-1] == 'A':
            v1 += 1
        elif v4[-1] == 'A':
            v2 += 1
        elif v4[0] == 'B':
            v3 += 1
    v5 = max(0, v1 - 1) + min(v2, v3)
    if (v2 > 0 or v3 > 0) and v1 > 0:
        v5 += 1
    v5 = max(0, v1 - 1)
    if v2 == v3:
        v5 += min(v2, v3)
        if (v2 > 0 or v3 > 0) and v1 != 0:
            v5 += 1
    elif v1 == 0:
        v5 += min(v2, v3)
    elif v2 > 0 or v3 > 0:
        v5 += min(v2, v3) + 1
    v6 = 0
    for v4 in a2:
        v6 += v4.count('AB')
    print(v5 + v6)
    return

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = [next(v1) for v4 in range(v2)]
    f1(v2, v3)
if __name__ == '__main__':
    f2()
