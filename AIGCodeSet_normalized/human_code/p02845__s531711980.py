import sys, collections as cl, bisect as bs
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
    if v1 != len(a2) and a2[v1] == a1:
        return True
    else:
        return False
'\ndef nibu(x,n,r):\n    ll = 0\n    rr = r\n    while True:\n        mid = (ll+rr)//2\n\n    if rr == mid:\n        return ll\n    if (ここに評価入れる):\n        rr = mid\n    else:\n        ll = mid+1\n'
v3 = f3()
v4 = f1()
v5 = []
v6 = 1
for v7 in range(v3):
    if v4[v7] == 0:
        v6 *= max(0, 3 - len(v5))
        v5.append(0)
    else:
        v8 = 0
        v9 = True
        for v10 in range(len(v5)):
            if v5[v10] == v4[v7] - 1:
                v8 += 1
                if v9 == True:
                    v5[v10] += 1
                    v9 = False
        v6 *= v8
        v6 %= v1
print(v6)
