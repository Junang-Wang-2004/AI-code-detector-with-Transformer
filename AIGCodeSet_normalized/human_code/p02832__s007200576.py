def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = 1
    v4 = 0
    for v5 in range(v1):
        if v3 == v2[v5]:
            v3 += 1
            v4 += 1
    if v4 == 0:
        print(-1)
    else:
        print(v1 - v4)
if __name__ == '__main__':
    f1()
