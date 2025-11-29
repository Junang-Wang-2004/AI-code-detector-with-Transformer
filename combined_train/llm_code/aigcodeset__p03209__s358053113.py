def f1():
    v1, v2 = R()
    v3 = lambda: sys.stdin.readline().strip()
    v4 = lambda: int(v3())
    v5 = lambda: list(map(int, v3().split()))
    v6 = lambda: map(int, v3().split())
    v7 = lambda: list(map(float, v3().split()))
    v8 = lambda: tuple(map(int, v3().split()))
    ' how to treat input\n    # single int: int(r())\n    # single string: r()\n    # single float: float(r())\n    # line int: R()\n    # line string: r().split()\n    # line (str, int, int): [j if i == 0 else int(j) for i, j in enumerate(r().split())]\n    # lines int: [R() for _ in range(n)]\n    '
    if __name__ != '__main__':
        sys.stdin = open('sample.txt')
    v1, v2 = v5()
    '\n    A_n = 2A_(n-1) + 3, A_0 = 1\n    B_n = 2B_n-1 + 1, B_0 = 0\n    '
    v9 = [1] * 50
    v10 = [1] * 50
    for v11 in range(1, 50):
        v9[v11] = 2 * v9[v11 - 1] + 3
    for v11 in range(1, 50):
        v10[v11] = 2 * v10[v11 - 1] + 1

    @lru_cache(maxsize=None)
    def burg(a1, a2):
        if a2 == 1:
            if a1 == 0:
                return 1
            return 0
        elif a2 <= 1 + v9[a1 - 1]:
            return 0 + burg(a1 - 1, a2 - 1)
        elif a2 == 2 + v9[a1 - 1]:
            return 1 + v10[a1 - 1]
        elif a2 <= 2 + 2 * v9[a1 - 1]:
            return 1 + v10[a1 - 1] + burg(a1 - 1, a2 - 2 - v9[a1 - 1])
        else:
            return v10[a1]
    print(burg(v1, v2))
    'memo: how to use defaultdict of list\n    # initialize\n    Dic = defaultdict(list)\n    # append / extend\n    Dic[x].append(y)\n    # three methods for loop: keys(), values(), items()\n    for k, v in Dic.items():\n    '
    "memo: how to solve binary problems\n    # to make binary digits text\n    >>> a = 5\n    >>> bin_str_a = format(a, '#06b')\n    >>> print(bin_str_a)\n    0b0101 # first 2 strings (='0b') indicates it is binary\n    "
    'memo: how to solve the problem\n    creating simple test/answer\n    greed\n    simple dp\n    graph\n    '
if __name__ == '__main__':
    f1()
