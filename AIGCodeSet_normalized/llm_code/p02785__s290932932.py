import math

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    if v2 >= v1:
        print(0)
        return
    v4 = 0
    v5 = sorted(v3, reverse=True)
    del v5[:v2]
    v4 += sum(v5)
    print(v4)
f1()
