from sortedcontainers import SortedList

class C1(object):

    def minOperations(self, a1, a2):
        """
        """

        def rebalance(a1, a2):
            if len(left) + 1 < len(right):
                v1, v2 = right.pop(0)
                a2 -= v1
                left.add((-v1, -v2))
                a1 += v1
            elif len(left) > len(right):
                v1, v2 = left.pop(0)
                a1 -= -v1
                right.add((-v1, -v2))
                a2 += -v1
            return (a1, a2)
        v1 = float('inf')
        v2 = SortedList()
        v3 = SortedList()
        v4 = v5 = 0
        for v6, v7 in enumerate(a1):
            if v2 and -v2[0][0] > v7:
                v2.add((-v7, -v6))
                v4 += v7
            else:
                v3.add((v7, v6))
                v5 += v7
            v4, v5 = rebalance(v4, v5)
            if v6 - (a2 - 1) >= 0:
                v1 = min(v1, v5 - (v3[0][0] if a2 % 2 else 0) - v4)
                v8, v9 = (v6 - (a2 - 1), a1[v6 - (a2 - 1)])
                if (-v9, -v8) in v2:
                    v2.remove((-v9, -v8))
                    v4 -= v9
                else:
                    v3.remove((v9, v8))
                    v5 -= v9
                v4, v5 = rebalance(v4, v5)
        return v1
