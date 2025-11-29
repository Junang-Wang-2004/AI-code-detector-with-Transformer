import sys, collections as cl, bisect as bs, heapq as hq
sys.setrecursionlimit(100000)
v1 = 10 ** 9 + 7
v2 = sys.maxsize

def f1():
    return list(map(int, input().split()))

def f2():
    return map(int, input().split())

def f3():
    return int(input())

def f4(a1):
    v1 = []
    v2 = a1[0]
    v3 = 1
    for v4 in range(len(a1) - 1):
        if v2 != a1[v4 + 1]:
            v1.append([v2, v3])
            v2 = a1[v4 + 1]
            v3 = 1
        else:
            v3 += 1
    v1.append([v2, v3])
    return v1

def f5(a1):
    return ' '.join(map(str, a1))

def f6(a1):
    return max(map(max, a1))

def f7(a1, a2):
    v1 = bs.bisect_left(a2, a1)
    if v1 != len(a2) and a2[v1][0] == a1:
        return True
    else:
        return False

def f8(a1, a2):
    v1 = dict()
    for v2 in range(0, len(a1) - a2 + 1):
        v3 = a1[v2:v2 + a2]
        v3 = ''.join(v3)
        if v3 in v1:
            if v1[v3] <= v2 - a2:
                return True
        else:
            v1[v3] = v2
    return False
v3 = f3()
v4 = list(input())
v5 = 0
v6 = v3 // 2
while True:
    v7 = -(-(v5 + v6) // 2)
    v8 = f8(v4, v7)
    if v5 == v7:
        break
    if v8:
        v5 = v7
    else:
        v6 = v7 - 1
print(v5)
