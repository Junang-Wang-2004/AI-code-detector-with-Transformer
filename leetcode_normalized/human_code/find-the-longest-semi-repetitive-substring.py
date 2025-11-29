class C1(object):

    def longestSemiRepetitiveSubstring(self, a1):
        """
        """
        v1 = v2 = v3 = 0
        for v4 in range(len(a1)):
            if v4 - 1 >= 0 and a1[v4 - 1] == a1[v4]:
                v2, v3 = (v3, v4)
            v1 = max(v1, v4 - v2 + 1)
        return v1
