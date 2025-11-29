def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = max(v2)
    v4 = len(bin(v3)) - 2
    for v5 in range(v1):
        v6 = len(bin(v2[v5])) - 2
        v7 = 0
        for v8 in range(v6):
            if v2[v5] >> v8 & 1 == 1:
                if v8 == v4 - 1 or v8 == 0:
                    v7 += pow(2, v8)
                else:
                    v7 -= pow(2, v8)
            else:
                if v8 == v4 - 1 or v8 == 0:
                    continue
                v7 += pow(2, v8)
        print(v7, end=' ')
if __name__ == '__main__':
    f1()
