v1 = 10 ** 9 + 7

def f1(a1, a2, a3, a4=True, a5=True):
    """
        l,r: l<r int if discrete else float
        f: function defined on [l,...,r] to {False,True}
        if discrete: f defined on Z; else: R
        if left: f satisfies that there uniquely exists d such that iff i<=d then f(i)
        else: iff i>=d then f(i) is True
        return d such as those above
    """
    assert a2 > a1
    if a4:
        assert isinstance(a1, int) and isinstance(a2, int)
    v1 = 1 if a4 else 10 ** (-12)
    if (not a5) ^ a3(a2):
        return a2 if a5 else a2 + 1
    elif a5 ^ a3(a1):
        return a1 - 1 if a5 else a1
    while a2 - a1 > v1:
        v2 = (a1 + a2) // 2 if a4 else (a1 + a2) / 2
        if (not a5) ^ a3(v2):
            a1 = v2
        else:
            a2 = v2
    return v2 if not a4 else a1 if a5 else a2

class C1(object):
    """
        construct: O(N)
        query:
            hash: O(1)
            lcp: O(logN)
            search: O(N)
    """
    v1 = 1007
    v2 = 10 ** 9
    v3 = 1009
    v4 = 10 ** 7

    def __init__(self, a1):
        v1 = len(a1)
        self.__s = a1
        self.__n = v1
        v2 = self.__base1
        v3 = self.__mod1
        v4 = self.__base2
        v5 = self.__mod2
        v6, v7 = ([0] * (v1 + 1), [0] * (v1 + 1))
        v8, v9 = ([1] * (v1 + 1), [1] * (v1 + 1))
        for v10 in range(v1):
            v6[v10 + 1] = (v6[v10] * v2 + ord(a1[v10])) % v3
            v7[v10 + 1] = (v7[v10] * v4 + ord(a1[v10])) % v5
            v8[v10 + 1] = v8[v10] * v2 % v3
            v9[v10 + 1] = v9[v10] * v4 % v5
        self.__H1 = v6
        self.__H2 = v7
        self.__P1 = v8
        self.__P2 = v9

    @property
    def str(self):
        return self.__s

    @property
    def len(self):
        return self.__n

    def hash(self, a1, a2=None):
        """
            l,r: int (0<=l<=r<=n)
            return (hash1,hash2) of S[l:r]
        """
        v1 = self.__mod1
        v2 = self.__mod2
        if a2 is None:
            a2 = self.__n
        assert 0 <= a1 <= a2 <= self.__n
        v4 = (self.__H1[a2] - self.__P1[a2 - a1] * self.__H1[a1] % v1) % v1
        v5 = (self.__H2[a2] - self.__P2[a2 - a1] * self.__H2[a1] % v2) % v2
        return (v4, v5)

    @classmethod
    def lcp(cls, a1, a2, a3, a4, a5=None, a6=None):
        """
            rh1,rh2: RollingHash object
            l1,l2,r1,r2: int 0<=l1<=r1<=r1.len, 0<=l2<=r2<=rh2.len
            return lcp length between rh1[l1:r1] and rh2[l2:r2]
        """
        if a5 is None:
            a5 = a1.__n
        if a6 is None:
            a6 = a2.__n
        assert 0 <= a3 <= a5 <= a1.__n and 0 <= a4 <= a6 <= a2.__n
        v3 = 0
        v4 = min(a5 - a3, a6 - a4)
        if a1.hash(a3, a3 + v4) == a2.hash(a4, a4 + v4):
            return v4
        while v4 - v3 > 1:
            v5 = (v3 + v4) // 2
            if a1.hash(a3, a3 + v5) == a2.hash(a4, a4 + v5):
                v3 = v5
        else:
            v4 = v5
        return v3

    @classmethod
    def search(cls, a1, a2):
        """
        pattern,text: RollingHash object
        return list of index i's satisfying text[i:] starts with pattern
        """
        v1 = a2.__n
        v2 = a1.__n
        v3 = []
        for v4 in range(v1 - v2 + 1):
            if a2.hash(v4, v4 + v2) == a1.hash(0, v2):
                v3.append(v4)
        return v3
if __name__ == '__main__':
    v2 = int(input())
    v3 = input()
    v4 = C1(v3)

    def f7(a1):
        v1 = {v4.hash(i, i + a1): -1 for v2 in range(v2 - a1 + 1)}
        for v2 in range(v2 - a1 + 1):
            v3 = v4.hash(v2, v2 + a1)
            if v1[v3] != -1:
                if v2 - v1[v3] >= a1:
                    return True
            else:
                v1[v3] = v2
        return False
    print(f1(0, v2, f7))
