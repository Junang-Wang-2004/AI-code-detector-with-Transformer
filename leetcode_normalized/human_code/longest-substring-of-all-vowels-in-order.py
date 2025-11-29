class C1(object):

    def longestBeautifulSubstring(self, a1):
        """
        """
        v1 = 0
        v2 = v3 = 1
        for v4 in range(len(a1) - 1):
            if a1[v4] > a1[v4 + 1]:
                v2 = v3 = 1
            else:
                v2 += 1
                v3 += int(a1[v4] < a1[v4 + 1])
            if v3 == 5:
                v1 = max(v1, v2)
        return v1
