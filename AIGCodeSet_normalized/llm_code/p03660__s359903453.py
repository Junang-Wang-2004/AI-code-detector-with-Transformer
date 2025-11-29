def f1(a1=''):
    """ convenient functions
    # for i, a in enumerate(iterable)
    # q, mod = divmod(a, b)
    # divmod(x, y) returns the tuple (x//y, x%y)
    # Higher-order function: reduce(operator.mul, xyz_count, 1)
    # manage median(s) using two heapq https://atcoder.jp/contests/abc127/tasks/abc127_f
    """
    'convenient decorator\n    # @functools.lru_cache():\n    # to facilitate use of recursive function\n        # ex:\n        # from functools import lru_cache\n        # import sys\n        # sys.setrecursionlimit(10**9)\n        # @lru_cache(maxsize=None)\n        # def fib(n):\n        #     if n < 2:\n        #         return n\n        #     return fib(n-1) + fib(n-2)\n        # print(fib(1000))\n    '
    import sys
    sys.setrecursionlimit(10 ** 7)
    from itertools import accumulate, combinations, permutations, product
    from math import factorial, ceil, floor, sqrt

    def factorize(a1):
        """return the factors of the Arg and count of each factor
        
        Args:
            n (long): number to be resolved into factors
        
        Returns:
            list of tuples: factorize(220) returns [(2, 2), (5, 1), (11, 1)]
        """
        v1 = []
        v2, v3 = (2, 0)
        while v2 * v2 <= a1:
            while a1 % v2 == 0:
                a1 = a1 // v2
                v3 = v3 + 1
            if v3 > 0:
                v1.append((v2, v3))
            v2, v3 = (v2 + 1, 0)
        if a1 > 1:
            v1.append((a1, 1))
        return v1

    def combinations_count(a1, a2):
        """Return the number of selecting r pieces of items from n kinds of items.
        
        Args:
            n (long): number
            r (long): number
        
        Raises:
            Exception: not defined when n or r is negative
        
        Returns:
            long: number
        """
        if a1 < 0 or a2 < 0:
            raise Exception('combinations_count(n, r) not defined when n or r is negative')
        if a1 - a2 < a2:
            a2 = a1 - a2
        if a2 < 0:
            return 0
        if a2 == 0:
            return 1
        if a2 == 1:
            return a1
        v2 = [a1 - a2 + k + 1 for v3 in range(a2)]
        v4 = [v3 + 1 for v3 in range(a2)]
        for v5 in range(2, a2 + 1):
            v6 = v4[v5 - 1]
            if v6 > 1:
                v7 = (a1 - a2) % v5
                for v3 in range(v5 - 1, a2, v5):
                    v2[v3 - v7] /= v6
                    v4[v3] /= v6
        v8 = 1
        for v3 in range(a2):
            if v2[v3] > 1:
                v8 *= int(v2[v3])
        return v8

    def combinations_with_replacement_count(a1, a2):
        """Return the number of selecting r pieces of items from n kinds of items allowing individual elements to be repeated more than once.
        
        Args:
            n (long): number
            r (long): number
        
        Raises:
            Exception: not defined when n or r is negative
        
        Returns:
            long: number
        """
        if a1 < 0 or a2 < 0:
            raise Exception('combinations_with_replacement_count(n, r) not defined when n or r is negative')
        elif a1 == 0:
            return 1
        else:
            return combinations_count(a1 + a2 - 1, a2)
    from bisect import bisect_left, bisect_right
    from collections import deque, Counter, defaultdict
    from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest, nsmallest
    from copy import deepcopy, copy
    import operator
    from operator import itemgetter
    from functools import reduce, lru_cache

    def chmin(a1, a2):
        """change minimum
        if x > y, x = y and return (x, True).
        convenient when solving problems of dp[i]
        
        Args:
            x (long): current minimum value
            y (long): potential minimum value
        
        Returns:
            (x, bool): (x, True) when updated, else (x, False)
        """
        if a1 > a2:
            a1 = a2
            return (a1, True)
        else:
            return (a1, False)

    def chmax(a1, a2):
        """change maximum
        if x < y, x = y and return (x, True).
        convenient when solving problems of dp[i]
        
        Args:
            x (long): current maximum value
            y (long): potential maximum value
        
        Returns:
            (x, bool): (x, True) when updated, else (x, False)
        """
        if a1 < a2:
            a1 = a2
            return (a1, True)
        else:
            return (a1, False)
    from fractions import gcd

    def gcds(a1):
        return reduce(gcd, a1)

    def lcm(a1, a2):
        return a1 * a2 // gcd(a1, a2)

    def lcms(a1):
        return reduce(lcm, a1, 1)

    def make_divisors(a1, a2=False):
        """create list of divisors
        
        Args:
            number (int): number from which list of divisors is created
            reversed (bool, optional): ascending order if False. Defaults to False.
        
        Returns:
            list: list of divisors
        """
        v1 = set()
        for v2 in range(1, int(a1 ** 0.5) + 1):
            if a1 % v2 == 0:
                v1.add(v2)
                v1.add(a1 // v2)
        return sorted(list(v1), reverse=a2)
    v1 = 10 ** 18
    v2 = 10 ** 9 + 7
    v3 = list('abcdefghijklmnopqrsruvwxyz')
    v4 = lambda a, n, p=v2: pow(a, n, p)

    def modinv(a1, a2=v2):
        return v4(a1, a2 - 2, a2)

    def modinv_list(a1, a2=v2):
        if a1 <= 1:
            return [0, 1][:a1 + 1]
        else:
            v1 = [0, 1]
            for v2 in range(2, a1 + 1):
                v1 += [v1[a2 % v2] * (a2 - int(a2 / v2)) % a2]
            return v1

    def modfactorial_list(a1, a2=v2):
        if a1 == 0:
            return [1]
        else:
            v1 = [0] * (a1 + 1)
            v2 = 1
            for v3 in range(1, a1 + 1):
                v2 = v2 * v3 % a2
                v1[v3] = v2
            return v1

    def modcomb(a1, a2, a3=[], a4=v2):
        from math import factorial
        if a1 < 0 or a2 < 0 or a1 < a2:
            return 0
        if a1 == 0 or a2 == 0:
            return 1
        if len(a3) <= a1:
            v1 = factorial(a1) % a4
            v2 = factorial(a2) % a4
            v3 = factorial(a1 - a2) % a4
        else:
            v1 = a3[a1]
            v2 = a3[a2]
            v3 = a3[a1 - a2]
        return v1 * v4(v2, a4 - 2, a4) * v4(v3, a4 - 2, a4) % a4

    def modadd(a1, a2, a3=v2):
        return (a1 + a2) % v2

    def modsub(a1, a2, a3=v2):
        return (a1 - a2) % a3

    def modmul(a1, a2, a3=v2):
        return a1 % a3 * (a2 % a3) % a3

    def moddiv(a1, a2, a3=v2):
        return modmul(a1, v4(a2, a3 - 2, a3))

    class UnionFindTree:
        """union find tree class
        TODO: fix this description...
        how to use (example):
        >>  uf = UnionFindTree(N) 
        >>  if uf.find_root(a) == uf.find_root(b):
        >>      do something
        >>  else:
        >>      do something
        >>      uf.unite(a, b)
        """

        def __init__(self, a1):
            self.root = [-1] * (a1 + 1)
            self.rank = [0] * (a1 + 1)
            self.connected_num = [1] * (a1 + 1)

        def find_root(self, a1):
            v1 = self.root
            while v1[a1] != -1:
                a1 = v1[a1]
            return a1

        def unite(self, a1, a2):
            v1 = self.root
            v2 = self.rank
            v3 = self.connected_num
            v4 = self.find_root
            v5 = v4(a1)
            v6 = v4(a2)
            if v5 != v6:
                if v2[v5] < v2[v6]:
                    v1[v5] = v6
                    v5, v6 = (v6, v5)
                else:
                    if v2[v5] == v2[v6]:
                        v2[v5] += 1
                    v1[v6] = v5
                v3[v5] += v3[v6]

    class SegTree:
        """
        ref: https://qiita.com/takayg1/items/c811bd07c21923d7ec69
        init(init_val, ide_ele): 配列init_valで初期化 O(N)
        update(k, x): k番目の値をxに更新 O(logN)
        query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
        """

        def __init__(self, a1, a2, a3):
            """
            init_val: 配列の初期値
            segfunc: 区間にしたい操作
            ide_ele: 単位元
            n: 要素数
            num: n以上の最小の2のべき乗
            tree: セグメント木(1-index)
            """
            v1 = len(a1)
            self.segfunc = a2
            self.ide_ele = a3
            self.num = 1 << (v1 - 1).bit_length()
            self.tree = [a3] * 2 * self.num
            for v2 in range(v1):
                self.tree[self.num + v2] = a1[v2]
            for v2 in range(self.num - 1, 0, -1):
                self.tree[v2] = self.segfunc(self.tree[2 * v2], self.tree[2 * v2 + 1])

        def update(self, a1, a2):
            """
            k番目の値をxに更新
            k: index(0-index)
            x: update value
            """
            a1 += self.num
            self.tree[a1] = a2
            while a1 > 1:
                self.tree[a1 >> 1] = self.segfunc(self.tree[a1], self.tree[a1 ^ 1])
                a1 >>= 1

        def query(self, a1, a2):
            """
            [l, r)のsegfuncしたものを得る
            l: index(0-index)
            r: index(0-index)
            """
            v1 = self.ide_ele
            a1 += self.num
            a2 += self.num
            while a1 < a2:
                if a1 & 1:
                    v1 = self.segfunc(v1, self.tree[a1])
                    a1 += 1
                if a2 & 1:
                    v1 = self.segfunc(v1, self.tree[a2 - 1])
                a1 >>= 1
                a2 >>= 1
            return v1

    def BellmanFord(a1, a2, a3, a4, a5, a6=-1, a7=False):
        """to calculate furthest or shortest length between vertex_start and vertex_end using BellmanFord algorithm
        
        Args:
            N (int): number of vertices
            M (int): number of edges
            ABC (list): [(ai, bi, ci) for _ in range(N)] where i-th edge is directed from vertex ai to vertex bi and the length is ci 
            vertex_start (int): start vertex. usually use 0.
            vertex_end (int): end vertex. usually use N-1.
            value_if_inf (int or string as you like, optional): value you want when the furthest (or shortest) distance is infinite (or -infinite). Defaults to -1.
            find_shortest (bool, optional): choose False to find furthest path. Defaults to False.
        
        Returns:
            int or string: normally int (but can be str if you set value_if_inf to str)
            
        Example:
                N, M, P = R()
                ABC = [R() for _ in range(M)]
                ABC = [(a-1, b-1, c-P) for a, b, c in ABC]
                print(BellmanFord(N, M, ABC, 0, N-1, value_if_inf = 'inf'))

        """

        def make_reachable_list(a1, a2, a3, a4, a5):
            v1 = defaultdict(list)
            v2 = defaultdict(list)
            v3 = [False] * a1
            v4 = [False] * a1
            v3[a4] = True
            v4[a5] = True
            v5 = [False] * a1
            v6 = []
            v7 = []
            for v8, v9, v10 in a3:
                v1[v8].append(v9)
                v2[v9].append(v8)
                if v8 == a4:
                    v6.append(v9)
                    v3[v9] = True
                if v9 == a5:
                    v7.append(v8)
                    v4[v8] = True
            while v6:
                v11 = v6.pop()
                for v12 in v1[v11]:
                    if not v3[v12]:
                        v3[v12] = True
                        v6.append(v12)
            while v7:
                v11 = v7.pop()
                for v12 in v2[v11]:
                    if not v4[v12]:
                        v4[v12] = True
                        v7.append(v12)
            for v12 in range(a1):
                v5[v12] = v3[v12] and v4[v12]
            return v5
        v1 = make_reachable_list(a1, a2, a3, a4, a5)
        if a7:
            v2 = [v1 for v3 in range(a1)]
        else:
            v2 = [-v1 for v3 in range(a1)]
        v2[a4] = 0
        for v3 in range(a1):
            v4 = False
            for v5, v6, v7 in a3:
                if not v1[v5]:
                    continue
                elif a7:
                    v8 = v2[v5] + v7 < v2[v6]
                else:
                    v8 = v2[v5] + v7 > v2[v6]
                if v2[v5] != v1 and v8:
                    v2[v6] = v2[v5] + v7
                    v4 = True
                    if v3 == a1 - 1:
                        return a6
            if not v4:
                break
        return v2[a5]

    def warshall_floyd(a1, a2, a3=False):
        v1 = [[float('inf')] * a1 for v2 in range(a1)]
        for v3, v4, v5 in a2:
            if a3:
                v3 = v3 - 1
                v4 = v4 - 1
            v1[v3][v4] = v5
            v1[v4][v3] = v5
        for v2 in range(a1):
            v1[v2][v2] = 0
        for v6 in range(a1):
            for v2 in range(a1):
                for v7 in range(a1):
                    v1[v2][v7] = min(v1[v2][v7], v1[v2][v6] + v1[v6][v7])
        return v1
    " initialize variables and set inputs\n    # initialize variables\n        # to initialize list, use [0] * n\n        # to initialize two dimentional array:\n            # ex) [[0] * N for _ in range(N)]\n            # ex2) dp = [[0] * (N+1) for _ in range(W*2)]\n    # set inputs\n        # put inputs between specific values (almost as quickly)\n        # ex) S = [-INF] + [int(r()) for _ in range(A)] + [INF]\n        # open(0).read() is sometimes useful:\n        # ex) n, m, *x = map(int, open(0).read().split())\n        #     min(x[::2]) - max(x[1::2])\n        # ex2) *x, = map(int, open(0).read().split())\n        #     don't forget to add comma after *x if only one variable is used\n    # preprocessing\n        # transpose = [x for x in zip(*data)]\n        # ex) [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]\n        # flat = [flatten for inner in data for flatten in inner]\n        # ex) [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [1, 2, 3, 4, 5, 6, 7, 8, 9]\n    # calculate and output\n        # output pattern\n        # ex1) print(*l) => when l = [2, 5, 6], printed 2 5 6\n    "
    v5 = lambda: sys.stdin.readline().strip()
    v6 = lambda: int(v5())
    v7 = lambda: float(v5())
    v8 = lambda: list(map(int, v5().split()))
    v9 = lambda: v5().split()
    v10 = lambda: map(int, v5().split())
    v11 = lambda: list(map(float, v5().split()))
    v12 = lambda: tuple(map(int, v5().split()))
    ' how to treat input\n    # single int: int(r())\n    # single string: r()\n    # single float: float(r())\n    # line int: R()\n    # line string: r().split()\n    # line (str, int, int): [j if i == 0 else int(j) for i, j in enumerate(r().split())]\n    # lines int: [R() for _ in range(n)]\n    '
    if a1:
        sys.stdin = open(a1)
    v13 = v6()
    v14 = [v8() for v15 in range(v13 - 1)]
    v16 = [[] for v15 in range(v13)]
    for v17, v18 in v14:
        v16[v17 - 1].append(v18 - 1)
        v16[v18 - 1].append(v17 - 1)
    v19 = [(i, [0]) for v20 in v16[0]]
    v21 = [0] * v13
    v21[0] = 1
    while v19:
        v22, v23 = v19.pop()
        for v24 in v16[v22]:
            if v24 == v13 - 1:
                v25 = v23 + [v22, v13 - 1]
                break
            if v21[v24] == 0:
                v21[v24] = 1
                v19.append((v24, v23 + [v22]))
    v26 = v25[(len(v25) - 1) // 2]
    v27 = v25[(len(v25) - 1) // 2 + 1]
    v28 = 0
    v19 = [0]
    v21 = [0] * v13
    while v19:
        v22 = v19.pop()
        v28 += 1
        v21[v22] = 1
        for v24 in v16[v22]:
            if v24 == v27:
                continue
            elif not v21[v24]:
                v19.append(v24)
    if v28 > v13 - v28:
        print('Fennec')
    else:
        print('Snuke')
    'memo: how to use defaultdict of list\n    # initialize\n    Dic = defaultdict(list)\n    # append / extend\n    Dic[x].append(y)\n    # three methods for loop: keys(), values(), items()\n    for k, v in Dic.items():\n    '
    "memo: how to solve binary problems\n    # to make binary digits text\n    >>> a = 5\n    >>> bin_str_a = format(a, '#06b')\n    >>> print(bin_str_a)\n    0b0101 # first 2 strings (='0b') indicates it is binary\n    "
    'memo: how to solve the problem\n    creating simple test/answer\n    greed\n    simple dp\n    graph\n    '
if __name__ == '__main__':
    f1()
