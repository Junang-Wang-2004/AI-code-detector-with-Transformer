from sortedcontainers import SortedList

class C1(object):

    def minReverseOperations(self, a1, a2, a3, a4):
        """
        """
        v1 = [False] * a1
        for v2 in a3:
            v1[v2] = True
        v3 = 0
        v4 = [-1] * a1
        v4[a2] = v3
        v5 = [SortedList((v2 for v2 in range(0, a1, 2))), SortedList((v2 for v2 in range(1, a1, 2)))]
        v5[a2 % 2].remove(a2)
        v6 = [a2]
        v3 += 1
        while v6:
            v7 = []
            for a2 in v6:
                v9, v10 = (2 * max(a2 - (a4 - 1), 0) + (a4 - 1) - a2, 2 * min(a2 + (a4 - 1), a1 - 1) - (a4 - 1) - a2)
                for a2 in list(v5[v9 % 2].irange(v9, v10)):
                    if not v1[a2]:
                        v4[a2] = v3
                        v7.append(a2)
                    v5[v9 % 2].remove(a2)
            v6 = v7
            v3 += 1
        return v4
