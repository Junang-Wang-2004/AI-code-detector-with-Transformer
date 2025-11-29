def f1():
    v1, v2, *v3 = map(int, open(0).read().split())
    v4 = min((r - l + min(abs(l), abs(r)) for v5, v6 in zip(v3, v3[v2 - 1:])))
    print(v4)
if __name__ == '__main__':
    f1()
