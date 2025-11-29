class C1(object):

    def maxFreq(self, a1, a2, a3, a4):
        """
        """
        v1 = {}
        for v2 in range(a3 - 1, len(a1)):
            v3 = a1[v2 - a3 + 1:v2 + 1]
            if v3 in v1:
                v1[v3] += 1
            elif len(collections.Counter(v3)) <= a2:
                v1[v3] = 1
        return max(list(v1.values()) or [0])
