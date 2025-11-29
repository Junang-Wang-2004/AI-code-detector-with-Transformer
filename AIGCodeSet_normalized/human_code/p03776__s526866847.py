from collections import defaultdict
from collections import Counter

def f1(a1, a2):
    v1 = 1
    for v2 in range(1, a1 + 1):
        v1 *= v2
    for v2 in range(1, a1 - a2 + 1):
        v1 //= v2
    for v2 in range(1, a2 + 1):
        v1 //= v2
    return v1

def f2():
    v1, v2, v3 = map(int, input().split())
    v4 = list(sorted(list(map(int, input().split()))))
    v5 = Counter(v4)
    v6 = sum(v4[-v2:])
    v7 = 0
    for v8 in range(v2, v3 + 1):
        v9 = v4[-v8:]
        if sum(v9) * v2 == v6 * v8:
            v10 = Counter(v9)
            v11 = 1
            for v12, v13 in v10.items():
                v11 *= f1(v5[v12], v13)
            v7 += v11
    print('{0:.7f}'.format(v6 / v2))
    print(v7)
if __name__ == '__main__':
    f2()
