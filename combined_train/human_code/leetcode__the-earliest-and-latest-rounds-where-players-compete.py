class C1(object):

    def earliestAndLatest(self, a1, a2, a3):
        """
        """

        def memoization(a1, a2, a3, a4):
            if (a1, a2, a3) not in a4:
                if a2 == a3:
                    return (1, 1)
                if a2 > a3:
                    a2, a3 = (a3, a2)
                v3 = [float('inf'), 0]
                for v4 in range(a2 + 1):
                    v5, v6, v7, v8 = (v4 + 1, a2 - v4, (a1 + 1) // 2, a1 // 2)
                    v9 = max(v6, a3 - (v8 - v6))
                    v10 = min(a3 - v5, v7 - v5 - 1)
                    for v11 in range(v9, v10 + 1):
                        v12 = memoization(v7, v4, v11, a4)
                        v3 = (min(v3[0], v12[0] + 1), max(v3[1], v12[1] + 1))
                a4[a1, a2, a3] = v3
            return a4[a1, a2, a3]
        return memoization(a1, a2 - 1, a1 - a3, {})
