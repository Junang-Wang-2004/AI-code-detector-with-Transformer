class C1(object):

    def countFairPairs(self, a1, a2, a3):
        """
        """

        def count(a1):
            v1 = 0
            v2, v3 = (0, len(a1) - 1)
            while v2 < v3:
                if a1[v2] + a1[v3] <= a1:
                    v1 += v3 - v2
                    v2 += 1
                else:
                    v3 -= 1
            return v1
        a1.sort()
        return count(a3) - count(a2 - 1)
