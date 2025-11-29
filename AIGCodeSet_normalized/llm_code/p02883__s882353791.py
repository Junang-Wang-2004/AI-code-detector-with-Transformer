import sys
sys.setrecursionlimit(10 ** 9)
v1 = 10 ** 20

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = list(map(int, input().split()))
    v3.sort()
    v4.sort(reverse=True)

    def c(a1):
        v1 = 0
        for v2 in range(v1):
            v3, v4 = (v3[v2], v4[v2])
            v5 = a1 // v4
            if not v3 <= v5:
                v1 += v3 - v5
        return v1 <= v2
    v5 = -10 ** 20
    v6 = 10 ** 20
    while v6 - v5 > 1:
        v7 = (v5 + v6) // 2
        if c(v7):
            v6 = v7
        else:
            v5 = v7
    print(v6)
if __name__ == '__main__':
    f1()
