from collections import defaultdict
from sortedcontainers import SortedList

class C1:

    def maximumCount(self, a1, a2):
        v1 = 100010
        v2 = list(range(v1))
        for v3 in range(2, int(v1 ** 0.5) + 1):
            if v2[v3] == v3:
                for v4 in range(v3 * v3, v1, v3):
                    if v2[v4] == v4:
                        v2[v4] = v3

        def isprime(a1):
            return 1 <= a1 < v1 and v2[a1] == a1
        v5 = len(a1)
        v6 = defaultdict(SortedList)

        class RangeAddMaxQuery:

            def __init__(self, a1):
                self.size = a1
                self.tre = [0] * (4 * a1 + 10)
                self.lzy = [0] * (4 * a1 + 10)

            def _push(self, a1, a2, a3):
                if self.lzy[a1]:
                    self.tre[a1] += self.lzy[a1]
                    if a2 < a3:
                        self.lzy[2 * a1] += self.lzy[a1]
                        self.lzy[2 * a1 + 1] += self.lzy[a1]
                    self.lzy[a1] = 0

            def _modify(self, a1, a2, a3, a4=1, a5=0, a6=None):
                if a6 is None:
                    a6 = self.size - 1
                self._push(a4, a5, a6)
                if a5 > a2 or a6 < a1 or a5 > a6:
                    return
                if a1 <= a5 and a6 <= a2:
                    self.lzy[a4] += a3
                    self._push(a4, a5, a6)
                    return
                v2 = (a5 + a6) // 2
                self._modify(a1, a2, a3, 2 * a4, a5, v2)
                self._modify(a1, a2, a3, 2 * a4 + 1, v2 + 1, a6)
                self.tre[a4] = max(self.tre[2 * a4], self.tre[2 * a4 + 1])

            def _qry(self, a1, a2, a3=1, a4=0, a5=None):
                if a5 is None:
                    a5 = self.size - 1
                self._push(a3, a4, a5)
