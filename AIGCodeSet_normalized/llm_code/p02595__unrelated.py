import math

def f1(a1, a2):
    v1 = 0
    for v2 in a1:
        v3, v4 = v2
        if math.sqrt(v3 ** 2 + v4 ** 2) <= a2:
            v1 += 1
    return v1

def f2():
    v1, v2 = map(int, input().split())
    v3 = []
    for v4 in range(v1):
        v5, v6 = map(int, input().split())
        v3.append((v5, v6))
    print(f1(v3, v2))
if __name__ == '__main__':
    f2()
