class C1(object):

    def maximumScore(self, a1, a2):
        """
        """
        v1 = v2 = a1[a2]
        v3 = v4 = a2
        while v3 - 1 >= 0 or v4 + 1 < len(a1):
            if (a1[v3 - 1] if v3 - 1 >= 0 else 0) <= (a1[v4 + 1] if v4 + 1 < len(a1) else 0):
                v4 += 1
            else:
                v3 -= 1
            v2 = min(v2, a1[v3], a1[v4])
            v1 = max(v1, v2 * (v4 - v3 + 1))
        return v1
