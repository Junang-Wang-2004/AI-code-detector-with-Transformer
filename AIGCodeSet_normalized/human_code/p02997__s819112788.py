import sys

def f1():
    v1 = 1000000007
    v2 = float('inf')
    sys.setrecursionlimit(10 ** 6)

    def input():
        return sys.stdin.readline().rstrip()

    def ii():
        return int(input())

    def mi():
        return map(int, input().split())

    def mi_0():
        return map(lambda x: int(x) - 1, input().split())

    def lmi():
        return list(map(int, input().split()))

    def lmi_0():
        return list(map(lambda x: int(x) - 1, input().split()))

    def li():
        return list(input())
    v3, v4 = mi()
    v5 = (v3 - 1) * (v3 - 2) // 2
    if v4 > v5:
        print(-1)
    else:
        v6 = v3 - 1 + (v5 - v4)
        print(v6)
        for v7 in range(2, v3 + 1):
            print('1 {}'.format(v7))
        v8 = v5 - v4
        for v9 in range(2, v3 + 1):
            for v10 in range(v9 + 1, v3 + 1):
                if v8 > 0:
                    print('{} {}'.format(v9, v10))
                    v8 -= 1
                else:
                    exit()
if __name__ == '__main__':
    f1()
