import collections

class C1(object):

    def averageHeightOfBuildings(self, a1):
        """
        """
        v1 = collections.defaultdict(lambda: (0, 0))
        for v2, v3, v4 in a1:
            v1[v2] = (v1[v2][0] + 1, v1[v2][1] + v4)
            v1[v3] = (v1[v3][0] - 1, v1[v3][1] - v4)
        v5 = []
        v6 = v7 = 0
        v8 = -1
        for v9, (v10, v4) in sorted(v1.items()):
            if v7:
                if v5 and v5[-1][1] == v8 and (v5[-1][2] == v6 // v7):
                    v5[-1][1] = v9
                else:
                    v5.append([v8, v9, v6 // v7])
            v6 += v4
            v7 += v10
            v8 = v9
        return v5
