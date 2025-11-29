class C1(object):

    def alternatingSubarray(self, a1):
        """
        """
        v1 = v2 = -1
        for v3 in range(len(a1) - 1):
            if v2 != -1 and a1[v3 - 1] == a1[v3 + 1]:
                v2 += 1
            else:
                v2 = 2 if a1[v3 + 1] - a1[v3] == 1 else -1
            v1 = max(v1, v2)
        return v1
