import sys
v1 = sys.stdin

def f1():
    return v1.readline().rstrip()

def f2():
    return int(f1())

def f3():
    return list(map(int, v1.readline().split()))

def f4(a1, a2):
    while a2:
        a1, a2 = (a2, a1 % a2)
    return a1

def f5():
    v1 = f2()
    v2 = f3()
    v3 = [1] * v1
    v3[0] = v2[0]
    v4 = [1] * v1
    v4[v1 - 1] = v2[v1 - 1]
    for v5 in range(1, v1):
        v3[v5] = f4(v3[v5 - 1], v2[v5])
    for v5 in list(range(0, v1 - 1))[::-1]:
        v4[v5] = f4(v4[v5 + 1], v2[v5])
    v6 = max(v4[1], v3[v1 - 2])
    for v5 in range(1, v1 - 1):
        v6 = max(v6, f4(v3[v5 - 1], v4[v5 + 1]))
    print(v6)
if __name__ == '__main__':
    f5()
