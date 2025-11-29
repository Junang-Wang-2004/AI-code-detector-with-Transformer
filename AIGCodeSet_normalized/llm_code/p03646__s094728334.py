import sys, bisect as bs
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
v3 = f3()
print(10 ** 5)
v4 = [i + v3 // 10 ** 5 for v5 in range(10 ** 5)]
for v5 in range(N - 1):
    if v5 + 1 <= v3 % 10 ** 5:
        v4[v5] += N - v3 % 10 ** 5 + 1
    else:
        v4[v5] -= v3 % 10 ** 5
print(f5(v4))
