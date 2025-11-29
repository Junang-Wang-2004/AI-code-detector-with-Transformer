class C1(object):

    def countMajoritySubarrays(self, a1, a2):
        """
        """
        v1 = [0] * (2 * len(a1) + 1 + 1)
        v2 = [0] * (2 * len(a1) + 1 + 1)
        v2[0] = v1[0] = 1
        v3 = v4 = 0
        for v5 in a1:
            v4 += +1 if v5 == a2 else -1
            v1[v4] += 1
            v2[v4] = v2[v4 - 1] + v1[v4]
            v3 += v2[v4 - 1]
        return v3
