v1 = 10 ** 9 + 7

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = list(map(int, input().split()))
    v5 = [(v3[i] - v3[i - 1]) * (i + 1) * (v1 - i) for v6 in range(v1)]
    v7 = [(v4[v6] - v4[v6 - 1]) * (v6 + 1) * (v2 - v6) for v6 in range(v2)]
    v8 = sum(v5) + sum(v7)
    print(v8 % v1)
if __name__ == '__main__':
    f1()
