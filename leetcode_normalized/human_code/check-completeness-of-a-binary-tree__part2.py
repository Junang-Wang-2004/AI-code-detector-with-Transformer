class C1(object):

    def isCompleteTree(self, a1):
        """
        """
        v1, v2 = ([], [(a1, 1)])
        v3 = 0
        while v2:
            v3 += len(v2)
            v4 = []
            for v5, v6 in v2:
                if not v5:
                    continue
                v4.append((v5.left, 2 * v6))
                v4.append((v5.right, 2 * v6 + 1))
            v1, v2 = (v2, v4)
        return v1[-1][1] == v3
