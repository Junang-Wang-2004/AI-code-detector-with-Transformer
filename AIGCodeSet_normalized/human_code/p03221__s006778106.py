v1 = 10 ** 9 + 7

def f1():
    return list(map(int, input().split()))

def f2():
    v1, v2 = f1()
    from collections import defaultdict
    import bisect
    v3 = [list(map(int, input().split())) for v4 in range(v2)]
    v5 = defaultdict(list)
    for v6, v7 in sorted(v3):
        v5[v6] += [v7]
    for v6, v7 in v3:
        v8 = bisect.bisect_right(v5[v6], v7)
        print('%06d%06d' % (v6, v8))
if __name__ == '__main__':
    f2()
