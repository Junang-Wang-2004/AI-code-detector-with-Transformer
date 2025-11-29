import sys

def f1(a1, a2):
    a1, a2 = (max(a1, a2), min(a1, a2))
    while a1 % a2 > 0:
        a1, a2 = (a2, a1 % a2)
    return a2

def f2():
    input = sys.stdin.readline
    v1 = int(input())
    v2 = [int(a) for v3 in input().split()]
    v4 = 10 ** 9 + 7
    v5 = v2[0]
    v6 = v2[0]
    for v7 in range(1, v1):
        v5 = f1(v6, v2[v7])
        v6 *= v2[v7] * pow(v5, v4 - 2, v4) % v4
        v6 %= v4
    v8 = 0
    for v3 in v2:
        v8 += v6 * pow(v3, v4 - 2, v4) % v4
        v8 %= v4
    print(v8)
    return 0
if __name__ == '__main__':
    f2()
