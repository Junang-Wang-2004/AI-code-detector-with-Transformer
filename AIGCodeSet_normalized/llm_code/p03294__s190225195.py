def f1():
    f2()

def f2():
    v1 = int(input())
    v2 = [int(x) for v3 in input().split(' ')]
    v4 = -1
    v5 = max(v2) * v1
    for v6 in range(v5):
        v4 = max(v4, f3(v6, v2))
    print(v4)

def f3(a1, a2):
    v1 = 0
    for v2 in a2:
        v1 += a1 % v2
    return v1
if __name__ == '__main__':
    f1()
