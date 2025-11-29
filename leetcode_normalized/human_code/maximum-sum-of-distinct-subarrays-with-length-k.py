class C1(object):

    def maximumSubarraySum(self, a1, a2):
        """
        """
        v1 = v2 = v3 = 0
        v4 = set()
        for v5 in range(len(a1)):
            while a1[v5] in v4 or len(v4) == a2:
                v4.remove(a1[v2])
                v3 -= a1[v2]
                v2 += 1
            v4.add(a1[v5])
            v3 += a1[v5]
            if len(v4) == a2:
                v1 = max(v1, v3)
        return v1
