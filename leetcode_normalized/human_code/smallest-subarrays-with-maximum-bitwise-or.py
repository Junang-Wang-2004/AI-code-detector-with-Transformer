class C1(object):

    def smallestSubarrays(self, a1):
        """
        """
        v1 = [0] * len(a1)
        v2 = [-1] * max(max(a1).bit_length(), 1)
        for v3 in reversed(range(len(a1))):
            for v4 in range(len(v2)):
                if a1[v3] & 1 << v4:
                    v2[v4] = v3
            v1[v3] = max(max(v2) - v3 + 1, 1)
        return v1
