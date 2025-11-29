class C1(object):

    def validSubstringCount(self, a1, a2):
        """
        """
        v1 = [0] * 26
        v2 = 0
        for v3 in a2:
            v2 += int(v1[ord(v3) - ord('a')] == 0)
            v1[ord(v3) - ord('a')] += 1
        v4 = v5 = 0
        for v6 in range(len(a1)):
            v1[ord(a1[v6]) - ord('a')] -= 1
            v2 -= int(v1[ord(a1[v6]) - ord('a')] == 0)
            while not v2:
                v4 += len(a1) - v6
                v2 += int(v1[ord(a1[v5]) - ord('a')] == 0)
                v1[ord(a1[v5]) - ord('a')] += 1
                v5 += 1
        return v4
