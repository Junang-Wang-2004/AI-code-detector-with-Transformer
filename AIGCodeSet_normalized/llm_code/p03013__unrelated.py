v1 = 10 ** 9 + 7

def f1():
    v1, v2 = map(int, input().split())
    v3 = set((int(input()) for v4 in range(v2)))
    v5 = [0] * (v1 + 1)
    v5[0] = 1
    for v6 in range(1, v1 + 1):
        if v6 not in v3:
            v5[v6] = (v5[v6 - 1] + v5[v6 - 2]) % v1
    print(v5[v1])
f1()
