def f1():
    import sys
    sys.setrecursionlimit(10 ** 7)
    v1 = sys.stdin.readline
    v2 = v1().strip()
    v3 = v1().strip()
    v4 = 0
    for v5 in range(3):
        if v2[v5] == v3[v5]:
            v4 += 1
    print(v4)
if __name__ == '__main__':
    f1()
