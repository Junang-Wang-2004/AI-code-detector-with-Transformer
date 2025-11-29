class C1(object):

    def findMinimumTime(self, a1):
        """
        """
        a1.sort(key=lambda x: x[1])
        v1 = set()
        for v2, v3, v4 in a1:
            v4 -= sum((i in v1 for v5 in range(v2, v3 + 1)))
            for v5 in reversed(range(1, v3 + 1)):
                if v4 <= 0:
                    break
                if v5 in v1:
                    continue
                v1.add(v5)
                v4 -= 1
        return len(v1)
