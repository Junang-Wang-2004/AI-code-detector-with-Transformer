import sys
input = sys.stdin.readline

def f1():
    return int(input())

def f2():
    return map(int, input().split())

def f3():
    return list(map(int, input().split()))

def f4():
    v1 = 10 ** 9 + 7
    v2 = f1()
    v3 = f3()
    v3.sort(reverse=True)
    v4 = sum(v3) - v3[-1] - v3[-2] + v3[1]
    print(v4)
f4()
