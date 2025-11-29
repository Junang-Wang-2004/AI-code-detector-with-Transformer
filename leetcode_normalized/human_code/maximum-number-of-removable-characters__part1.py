class C1(object):

    def maximumRemovals(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4):
            v1 = set((a3[i] for v2 in range(a4)))
            v3 = 0
            for v2 in range(len(a1)):
                if v2 in v1 or a1[v2] != a2[v3]:
                    continue
                v3 += 1
                if v3 == len(a2):
                    return True
            return False
        v1, v2 = (0, len(a3))
        while v1 <= v2:
            v3 = v1 + (v2 - v1) // 2
            if not check(a1, a2, a3, v3):
                v2 = v3 - 1
            else:
                v1 = v3 + 1
        return v2
