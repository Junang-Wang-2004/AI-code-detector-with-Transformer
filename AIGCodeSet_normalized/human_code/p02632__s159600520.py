def f1():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    v1 = int(input())
    v2 = input()
    v3 = len(v2)
    v4 = 10 ** 9 + 7
    v5 = [0] * (v1 + 1)
    v6 = [0] * (v1 + 1)
    v7 = [0] * (v1 + 1)
    v5[0], v6[0] = (1, 1)
    v7[0] = 1
    for v8 in range(1, v1 + 1):
        v5[v8] = v5[v8 - 1] * 25
        v5[v8] %= v4
        v6[v8] = v6[v8 - 1] * 26
        v6[v8] %= v4
        v7[v8] = (v3 + v8 - 1) * v7[v8 - 1]
        v7[v8] *= pow(v8, v4 - 2, v4)
        v7[v8] %= v4
    v5.reverse()
    v7.reverse()
    v9 = 0
    for v8 in range(v1 + 1):
        v10 = v5[v8] * v6[v8] * v7[v8]
        v10 %= v4
        v9 += v10
        v9 %= v4
    print(v9)
if __name__ == '__main__':
    f1()
