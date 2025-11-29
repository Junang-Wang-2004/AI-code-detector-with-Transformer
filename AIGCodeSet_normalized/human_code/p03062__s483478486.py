def f1():
    v1 = int(input())
    v2 = list(map(int, input().split()))
    v3 = 0
    for v4 in v2:
        if v4 < 0:
            v3 += 1
    v5 = sum(map(abs, v2))
    if v3 % 2 == 0:
        print(v5)
    else:
        print(v5 - 2 * min(map(abs, v2)))
if __name__ == '__main__':
    f1()
