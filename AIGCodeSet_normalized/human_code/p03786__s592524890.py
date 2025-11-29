def f1():
    v1 = int(input())
    v2 = [int(i) for v3 in input().split()]
    v2.sort()
    v4 = 0
    v5 = 0
    for v3 in range(v1):
        v4 += v2[v3]
        v5 += 1
        if v3 == v1 - 1:
            break
        if v2[v3 + 1] <= v4 * 2:
            continue
        else:
            v5 = 0
    print(v5)
if __name__ == '__main__':
    f1()
