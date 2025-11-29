class C1(object):

    def countAlternatingSubarrays(self, a1):
        """
        """
        v1 = v2 = 0
        for v3 in range(len(a1)):
            if v3 - 1 >= 0 and a1[v3 - 1] == a1[v3]:
                v2 = 0
            v2 += 1
            v1 += v2
        return v1
