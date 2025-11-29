import sys

def f1(a1, a2):
    v1 = 0
    for v2, v3 in enumerate(a1):
        v1 += abs(v3 - (a2 + (v2 + 1)))
    return v1

def f2(a1, a2):
    v1 = []
    for v2, v3 in enumerate(a2):
        v1.append(v3 - (v2 + 1))
    return f1(a2, sorted(v1)[a1 // 2])

def f3():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    v3 = [int(next(v1)) for v4 in range(v2)]
    print(f2(v2, v3))
if __name__ == '__main__':
    f3()
