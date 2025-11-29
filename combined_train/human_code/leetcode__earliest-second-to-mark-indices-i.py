class C1(object):

    def earliestSecondToMarkIndices(self, a1, a2):
        """
        """

        def check(a1):
            v1 = [-1] * len(a1)
            for v2 in range(a1):
                v1[a2[v2] - 1] = v2
            if -1 in v1:
                return False
            v3 = 0
            for v2 in range(a1):
                if v2 != v1[a2[v2] - 1]:
                    v3 += 1
                    continue
                v3 -= a1[a2[v2] - 1]
                if v3 < 0:
                    return False
            return True
        v1, v2 = (sum(a1) + len(a1), len(a2))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if check(v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v1 if v1 <= len(a2) else -1
