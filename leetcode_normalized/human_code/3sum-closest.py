class C1(object):

    def threeSumClosest(self, a1, a2):
        """
        """
        v1, v2 = (0, float('inf'))
        a1.sort()
        for v3 in reversed(range(2, len(a1))):
            if v3 + 1 < len(a1) and a1[v3] == a1[v3 + 1]:
                continue
            v4, v5 = (0, v3 - 1)
            while v4 < v5:
                v6 = a1[v4] + a1[v5] + a1[v3]
                if v6 < a2:
                    v4 += 1
                elif v6 > a2:
                    v5 -= 1
                else:
                    return a2
                if abs(v6 - a2) < v2:
                    v2 = abs(v6 - a2)
                    v1 = v6
        return v1
