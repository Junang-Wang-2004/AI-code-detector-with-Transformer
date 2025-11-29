class C1(object):

    def countSubarrays(self, a1, a2):
        """
        """
        v1 = max(a1)
        v2 = (len(a1) + 1) * len(a1) // 2
        v3 = v4 = 0
        for v5 in range(len(a1)):
            v4 += int(a1[v5] == v1)
            while v4 == a2:
                v4 -= int(a1[v3] == v1)
                v3 += 1
            v2 -= v5 - v3 + 1
        return v2
