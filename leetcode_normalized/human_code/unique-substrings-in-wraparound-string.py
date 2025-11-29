class C1(object):

    def findSubstringInWraproundString(self, a1):
        """
        """
        v1 = [0] * 26
        v2, v3 = (0, 0)
        for v4 in range(len(a1)):
            v5 = ord(a1[v4]) - ord('a')
            if v4 > 0 and ord(a1[v4 - 1]) != (v5 - 1) % 26 + ord('a'):
                v3 = 0
            v3 += 1
            if v3 > v1[v5]:
                v2 += v3 - v1[v5]
                v1[v5] = v3
        return v2
