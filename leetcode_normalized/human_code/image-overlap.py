class C1(object):

    def largestOverlap(self, a1, a2):
        """
        """
        v1 = [0] * (2 * len(a1) - 1) ** 2
        for v2, v3 in enumerate(a1):
            for v4, v5 in enumerate(v3):
                if not v5:
                    continue
                for v6, v7 in enumerate(a2):
                    for v8, v9 in enumerate(v7):
                        if not v9:
                            continue
                        v1[(len(a1) - 1 + v2 - v6) * (2 * len(a1) - 1) + len(a1) - 1 + v4 - v8] += 1
        return max(v1)
