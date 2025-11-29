class C1(object):

    def countSubarrays(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if not (v3 - 1 >= 0 and a1[v3 - 1] < a1[v3]):
                v2 = v3
            v1 += v3 - v2 + 1
        return v1
