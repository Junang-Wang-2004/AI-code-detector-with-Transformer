def f1():
    v1, v2, v3 = map(int, input().split())
    v4, v5 = divmod(v3 * v2, v1)
    v6 = [str(v4)] * v1
    for v7 in range(v5):
        v6[v7] += '1'
    print(' '.join(v6))
if __name__ == '__main__':
    f1()
