def f1():
    return map(int, input().split())

def f2():
    return int(input())

def f3():
    v1, v2 = f1()
    v3 = [f2() for v4 in range(v1)]
    v3.sort()
    v5 = 10 ** 9
    for v6 in range(v1 - v2 + 1):
        v5 = min(v5, v3[v6 + v2 - 1] - v3[v6])
    print(v5)
if __name__ == '__main__':
    f3()
