import sys
v1 = float('inf')

def f1(a1: int):
    v1 = 50
    v2, v3 = divmod(a1, v1)
    v4 = [i + v2 for v5 in range(v1)]
    for v5 in range(v3):
        v4[v5] += v1
        for v6 in range(v1):
            if v5 == v6:
                continue
            v4[v6] -= 1
    print(v1)
    print(*v4, sep=' ')
    return

def f2():

    def iterate_tokens():
        for v1 in sys.stdin:
            for v2 in v1.split():
                yield v2
    v1 = iterate_tokens()
    v2 = int(next(v1))
    f1(v2)
if __name__ == '__main__':
    f2()
