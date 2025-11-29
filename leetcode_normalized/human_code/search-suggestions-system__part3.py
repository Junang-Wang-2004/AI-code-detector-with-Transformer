import bisect

class C1(object):

    def suggestedProducts(self, a1, a2):
        """
        """
        a1.sort()
        v1 = []
        v2 = ''
        for v3, v4 in enumerate(a2):
            v2 += v4
            v5 = bisect.bisect_left(a1, v2)
            v6 = []
            for v7 in range(v5, len(a1)):
                if not (v3 < len(a1[v7]) and a1[v7][v3] == v4):
                    break
                v6.append(a1[v7])
            a1 = v6
            v1.append(a1[:3])
        return v1
