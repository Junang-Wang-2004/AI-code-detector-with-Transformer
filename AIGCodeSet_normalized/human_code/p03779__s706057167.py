import sys
input = sys.stdin.readline

def f1():
    v1 = int(input())
    for v2 in range(v1 + 1):
        if v2 * (v2 + 1) / 2 >= v1:
            print(v2)
            return
f1()
