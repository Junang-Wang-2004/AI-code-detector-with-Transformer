def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = [v2[i] - i for v4 in range(v1)]
    v5 = f2(v3)
    print(sum([abs(v2[v4] - (v5 + v4)) for v4 in range(v1)]))

def f2(a1):
    v1 = min(a1)
    v2 = max(a1)
    v3 = 10 ** 10
    while True:
        if f3(a1, v1) >= f3(a1, v2):
            v4 = int((v1 + v2) / 2)
            v1 = v4
        else:
            v4 = int((v1 + v2) / 2)
            v2 = v4
        if v4 == v3:
            if min(f3(a1, v4), f3(a1, v4 + 1), f3(a1, v4 - 1)) == f3(a1, v4):
                return v4
            elif min(f3(a1, v4), f3(a1, v4 + 1), f3(a1, v4 - 1)) == f3(a1, v4 + 1):
                return v4 + 1
            else:
                return v4 - 1
        else:
            v3 = v4

def f3(a1, a2):
    return sum([abs(x - a2) for v1 in a1])
if __name__ == '__main__':
    f1()
