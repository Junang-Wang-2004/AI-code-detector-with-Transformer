class C1(object):

    def lengthOfLIS(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1)):
            v1.append(1)
            for v3 in range(v2):
                if a1[v3] < a1[v2]:
                    v1[v2] = max(v1[v2], v1[v3] + 1)
        return max(v1) if v1 else 0
