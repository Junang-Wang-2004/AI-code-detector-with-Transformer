from itertools import accumulate

def f1(a1):
    v1 = [n & 1 for v2 in range(a1 + 1)]
    v1[1] = 0
    v1[2] = 1
    v3 = [0] * (a1 + 1)
    v4 = 1
    while True:
        while not v1[v4]:
            v4 += 2
        if v4 * v4 > a1:
            for v5 in range(v4, a1 + 1, 2):
                if v1[v5 + 1 >> 1]:
                    v3[v5] = 1
            return v3
        if v1[v4 + 1 >> 1]:
            v3[v4] = 1
        for v5 in range(v4 * 2, a1 + 1, v4):
            v1[v5] = 0
        v4 += 2
v1 = f1(10 ** 5)
v2 = list(accumulate(v1))
v3 = int(input())
for v4 in range(v3):
    v5, v6 = map(int, input().split())
    print(v2[v6] - v2[v5 - 1])
