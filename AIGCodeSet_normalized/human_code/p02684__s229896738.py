def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = 1
    v5 = [-1] * v1
    v6 = 0
    while v5[v4 - 1] == -1:
        v5[v4 - 1] = v6
        v4 = v3[v4 - 1]
        v6 += 1
    v7 = v5[v4 - 1]
    v8 = v6
    v2 = min(v2, v7 + (v2 - v7) % (v8 - v7))
    v4 = 1
    for v9 in range(v2):
        v4 = v3[v4 - 1]
    print(v4)
if __name__ == '__main__':
    f1()
