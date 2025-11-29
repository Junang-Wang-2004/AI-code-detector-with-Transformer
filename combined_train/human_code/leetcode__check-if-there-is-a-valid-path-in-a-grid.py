class C1(object):

    def hasValidPath(self, a1):
        """
        """
        v1, v2, v3, v4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v5 = [[v3, v1], [v4, v2], [v3, v2], [v2, v1], [v3, v4], [v4, v1]]
        for v6, v7 in v5[a1[0][0] - 1]:
            if not (0 <= v6 < len(a1) and 0 <= v7 < len(a1[0])):
                continue
            v8, v9 = (0, 0)
            while v6 != len(a1) - 1 or v7 != len(a1[0]) - 1:
                for v10, v11 in v5[a1[v6][v7] - 1]:
                    v12, v13 = (v6 + v10, v7 + v11)
                    if v12 == v8 and v13 == v9 or not (0 <= v12 < len(a1) and 0 <= v13 < len(a1[0])) or (-v10, -v11) not in v5[a1[v12][v13] - 1]:
                        continue
                    v8, v9, v6, v7 = (v6, v7, v12, v13)
                    break
                else:
                    return False
            return True
        return len(a1) == len(a1[0]) == 1
