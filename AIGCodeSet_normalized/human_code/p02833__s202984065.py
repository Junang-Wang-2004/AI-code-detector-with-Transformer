from decimal import *
v1 = lambda: int(input())
v2 = lambda: map(int, input().split())
v3 = lambda: map(str, input().split())
v4 = lambda: str(input())
v5 = lambda: list(map(int, input().split()))
v6 = lambda: list(map(str, input().split()))

def f1():
    v1 = v1()
    v2 = 0
    if v1 % 2 == 1:
        print(0)
    else:
        for v3 in range(1, 30, 1):
            v4 = v1 // (2 * 5 ** v3)
            v2 += v4
        print(v2)
if __name__ == '__main__':
    f1()
