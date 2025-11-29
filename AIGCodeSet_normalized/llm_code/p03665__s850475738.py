import math

def f1(a1, a2):
    return math.factorial(a1) // (math.factorial(a1 - a2) * math.factorial(a2))
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = 0
    if v2 == 0:
        for v5 in range(0, v1 + 1, 2):
            v4 += f1(v1, v5)
    else:
        for v5 in range(1, v1 + 1, 2):
            v4 += f1(v1, v5)
    print(v4)
