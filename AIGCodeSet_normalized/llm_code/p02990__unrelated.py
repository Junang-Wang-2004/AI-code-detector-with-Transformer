def f1(a1, a2):
    v1 = [1] * (a2 + 1)
    for v2 in range(1, a1):
        for v3 in range(a2, 0, -1):
            v1[v3] = (v1[v3] + v1[v3 - 1]) % 1000000007
    return v1[a2]
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    print(f1(v1, v2))
