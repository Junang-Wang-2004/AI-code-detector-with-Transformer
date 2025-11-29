class C1(object):

    def longestIdealString(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v3 = ord(v2) - ord('a')
            v1[v3] = max((v1[i] for v4 in range(max(v3 - a2, 0), min(v3 + a2 + 1, 26)))) + 1
        return max(v1)
