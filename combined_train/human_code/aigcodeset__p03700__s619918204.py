import sys
v1 = sys.stdin.readline

def f1():
    v1, v2, v3 = map(int, v1().split())
    v4 = [int(v1()) for v5 in range(v1)]
    v6 = v2 - v3

    def calc(a1):
        v1 = 0
        for v2 in range(v1):
            v3 = v4[v2] - v3 * a1
            if 0 < v3:
                v1 += v3 // v6 if v3 % v6 == 0 else v3 // v6 + 1
        return v1 <= a1
    v7, v8 = (10 ** 9, 0)
    while 1 < v7 - v8:
        v9 = (v7 + v8) // 2
        if calc(v9):
            v7 = v9
        else:
            v8 = v9
    print(v7)
if __name__ == '__main__':
    f1()
