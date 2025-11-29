import sys
sys.setrecursionlimit(10 ** 6)
v1 = 10 ** 9 + 7

def f1(a1, a2):
    v1, v2 = map(int, a1().split())
    v3 = list(map(int, a1().split()))
    v4 = 0
    for v5 in range(v1):
        if v3[v5] < 0:
            v4 += 1
    v6 = 0
    v7 = 0
    v8 = 1
    v3 = sorted(v3, key=abs, reverse=True)
    v9 = 0
    for v5 in range(v1):
        if v2 == v7:
            break
        if v3[v5] < 0:
            if v2 - v7 > 1 and v6 < v4:
                if v6 % 2 == 1:
                    v8 = v8 * v9 * v3[v5] % v1
                    v7 += 2
                else:
                    v9 = v3[v5]
                v6 += 1
        else:
            v8 = v8 * v3[v5] % v1
            v7 += 1
    if v7 == v2:
        a2(v8)
        return
    v8 = 1
    v3 = sorted(v3, key=abs)
    v9 = 0
    for v5 in range(v2):
        v8 = v8 * v3[v5] % v1
    a2(v8)
if __name__ == '__main__':
    f1(sys.stdin.readline, print)
