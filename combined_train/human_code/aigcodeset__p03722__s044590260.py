import sys
v1 = 1 << 60

def f1():
    v1, v2 = map(int, input().split())
    v3 = [None] * v2
    for v4 in range(v2):
        v5, v6, v7 = map(int, sys.stdin.readline().split())
        v5, v6 = (v5 - 1, v6 - 1)
        v3[v4] = (v5, v6, -v7)
    v8 = f2(v1, v2, v3)
    if v8 is None:
        print('inf')
    else:
        print(-v8)

def f2(a1, a2, a3):
    v1 = [v1] * a1
    v1[0] = 0
    for v2 in range(a1 - 1):
        for v3, v4, v5 in a3:
            if v1[v3] + v5 < v1[v4]:
                v1[v4] = v1[v3] + v5
    for v2 in range(a1):
        for v3, v4, v5 in a3:
            if v1[v3] + v5 < v1[v4]:
                if v4 == a1 - 1:
                    return None
                v1[v4] = v1[v3] + v5
    return v1[a1 - 1]
if __name__ == '__main__':
    f1()
