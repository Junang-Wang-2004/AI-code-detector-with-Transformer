import sys
v1 = ['clipboard', 'file', 'key']
v2 = 1
v3 = v1[v2]
v4 = lambda: map(int, input().split())
v5 = lambda: list(v4())
v6 = 1000000007

def f1(a1):
    for v1 in range(a1 + 1):
        if 2 * a1 == v1 * (v1 + 1):
            return v1 + 1
        if 2 * a1 < v1 * (v1 + 1):
            return -1
    return -1

def f2():
    v1 = int(input())
    v2 = f1(v1)
    if v2 == -1:
        return 'No'
    print('Yes')
    print(v2)
    v3 = v2 - 1
    v4 = []
    v4.append(list(range(1, v3 + 1)))
    next = v3 + 1
    for v5 in range(v2 - 1):
        v6 = []
        for v7, v8 in enumerate(v4):
            v6.append(v8[len(v4) - 1])
        while len(v6) < v3:
            v6.append(next)
            next += 1
        v4.append(v6)
    for v8 in v4:
        print(v3, *v8)
v7 = False

def f3(a1):
    if v7:
        print(a1)

def f4():
    import clipboard
    v1 = clipboard.get()
    v2 = v1.splitlines()
    for v3 in v2:
        yield v3
if __name__ == '__main__':
    if sys.platform == 'ios':
        if v3 == v1[0]:
            v8 = f4()
            input = lambda: v8.__next__()
        elif v3 == v1[1]:
            sys.stdin = open('inputFile.txt')
        else:
            pass
        v7 = True
    else:
        pass
    v9 = f2()
    if v9 is not None:
        print(v9)
