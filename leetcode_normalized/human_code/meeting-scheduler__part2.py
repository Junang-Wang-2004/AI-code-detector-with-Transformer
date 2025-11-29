class C1(object):

    def minAvailableDuration(self, a1, a2, a3):
        """
        """
        a1.sort(key=lambda x: x[0])
        a2.sort(key=lambda x: x[0])
        v1, v2 = (0, 0)
        while v1 < len(a1) and v2 < len(a2):
            v3 = max(a1[v1][0], a2[v2][0])
            v4 = min(a1[v1][1], a2[v2][1])
            if v3 + a3 <= v4:
                return [v3, v3 + a3]
            if a1[v1][1] < a2[v2][1]:
                v1 += 1
            else:
                v2 += 1
        return []
