def f1():
    v1 = int(input())
    v2 = list(map(int, input().split(' ')))
    v3 = list(map(int, input().split(' ')))
    v4 = 0
    v5 = v2[v1]
    for v6, v7 in enumerate(reversed(v2[:v1])):
        v8 = v5 + v7
        v9 = v3[v1 - (v6 + 1)]
        v4 += min(v8, v9)
        if v9 <= v8:
            v5 = v7
        v5 = max(0, v8 - v5)
    print(v4)
if __name__ == '__main__':
    f1()
