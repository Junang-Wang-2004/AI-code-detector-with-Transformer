import sys
v1 = sys.stdin.read
v2 = sys.stdin.readline
v3 = sys.stdin.readlines
v4 = 10 ** 9 + 7
v5 = [1, 1]
v6 = [1, 1]
v7 = [0, 1]

def f1(a1, a2):
    for v1 in range(2, a1 + 1):
        v5.append(v5[-1] * v1 % a2)
        v7.append(-v7[a2 % v1] * (a2 // v1) % a2)
        v6.append(v6[-1] * v7[-1] % a2)

def f2(a1, a2, a3):
    if a1 < 0 or a2 < 0 or a2 > a1:
        return 0
    return v5[a1] * v6[a2] * v6[a1 - a2] % a3

def f3():
    v1, v2 = map(int, v2().split())
    f1(v1, v4)
    v3 = 0
    for v4 in range(min(v1 - 1, v2) + 1):
        v3 += f2(v1, v4, v4) * f2(v1 - 1, v4, v4)
        v3 %= v4
    print(v3)
if __name__ == '__main__':
    f3()
