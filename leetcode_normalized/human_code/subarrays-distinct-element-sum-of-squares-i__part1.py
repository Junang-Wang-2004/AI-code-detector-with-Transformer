import collections
from sortedcontainers import SortedList

class C1(object):

    def sumCounts(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        class BIT(object):

            def __init__(self, a1):
                self.__bit = [0] * (a1 + 1)

            def add(self, a1, a2):
                a1 += 1
                while a1 < len(self.__bit):
                    self.__bit[a1] = (self.__bit[a1] + a2) % v1
                    a1 += a1 & -a1

            def query(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 = (v2 + self.__bit[a1]) % v1
                    a1 -= a1 & -a1
                return v2

        def update(a1, a2):
            v1 = sl.bisect_left(idxs[x][-1])
            a1 = (a1 + a2 * (len(a1) * (2 * len(sl) - 1) - (2 * v1 + 1) * idxs[x][-1] - 2 * (bit.query(len(a1) - 1) - bit.query(idxs[x][-1])))) % v1
            bit.add(idxs[x][-1], a2 * idxs[x][-1])
            return a1
        v2 = collections.defaultdict(list)
        for v3 in reversed(range(len(a1))):
            v2[a1[v3]].append(v3)
        v4 = 0
        v5 = SortedList((v2[x][-1] for v6 in v2))
        v7 = len(a1) * len(v5) ** 2 % v1
        for v3, v6 in enumerate(v5):
            v7 = (v7 - (2 * v3 + 1) * v6) % v1
        v8 = BIT(len(a1))
        for v6 in v5:
            v8.add(v6, v6)
        for v6 in a1:
            v4 = (v4 + v7) % v1
            v7 = update(v7, -1)
            del v5[0]
            v2[v6].pop()
            if not v2[v6]:
                continue
            v5.add(v2[v6][-1])
            v7 = update(v7, +1)
        assert v7 == 0
        return v4
