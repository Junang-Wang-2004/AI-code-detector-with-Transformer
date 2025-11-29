from sortedcontainers import SortedList

class C1(object):

    def maxBalancedSubsequenceSum(self, a1):
        """
        """
        v1 = float('-inf')

        def query(a1, a2):
            v1 = a1.bisect_left((a2,))
            return a1[v1 - 1][1] if v1 - 1 >= 0 else v1

        def update(a1, a2, a3):
            v1 = a1.bisect_left((a2,))
            if v1 < len(a1) and a1[v1][0] == a2:
                if not a1[v1][1] < a3:
                    return
                del a1[v1]
            elif not (v1 - 1 < 0 or a1[v1 - 1][1] < a3):
                return
            a1.add((a2, a3))
            while v1 + 1 < len(a1) and a1[v1 + 1][1] <= a1[v1][1]:
                del a1[v1 + 1]
        v2 = SortedList()
        for v3, v4 in enumerate(a1):
            v5 = max(query(v2, v4 - v3 + 1), 0) + v4
            update(v2, v4 - v3, v5)
        return v2[-1][1]
