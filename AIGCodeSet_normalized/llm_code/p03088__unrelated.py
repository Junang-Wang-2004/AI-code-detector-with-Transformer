v1 = 10 ** 9 + 7

def f1():
    v1 = int(input())
    v2 = [[0] * 4 for v3 in range(v1 + 1)]
    v2[0][0] = 1
    for v4 in range(v1):
        for v5 in range(4):
            for v6 in range(4):
                if v5 == 1 and v6 == 2:
                    continue
                v2[v4 + 1][v6] = (v2[v4 + 1][v6] + v2[v4][v5]) % v1
    print(sum(v2[v1]) % v1)
f1()
