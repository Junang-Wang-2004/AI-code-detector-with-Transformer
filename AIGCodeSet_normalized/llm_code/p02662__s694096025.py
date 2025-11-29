v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [[0] * (v2 + 1) for v5 in range(v1 + 1)]

def f1():
    v4[0][0] = 1
    for v1 in range(1, v1 + 1):
        for v2 in range(0, v2 + 1):
            v4[v1][v2] += v4[v1 - 1][v2]
            if v2 - v3[v1 - 1] >= 0:
                v4[v1][v2] += v4[v1 - 1][v2 - v3[v1 - 1]]
    print(sum(v4[v1]) % 998244353)
if __name__ == '__main__':
    f1()
