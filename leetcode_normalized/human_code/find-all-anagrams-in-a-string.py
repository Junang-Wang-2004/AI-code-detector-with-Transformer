class C1(object):

    def findAnagrams(self, a1, a2):
        """
        """
        v1 = []
        v2 = [0] * 26
        for v3 in a2:
            v2[ord(v3) - ord('a')] += 1
        v4, v5 = (0, 0)
        while v5 < len(a1):
            v2[ord(a1[v5]) - ord('a')] -= 1
            while v4 <= v5 and v2[ord(a1[v5]) - ord('a')] < 0:
                v2[ord(a1[v4]) - ord('a')] += 1
                v4 += 1
            if v5 - v4 + 1 == len(a2):
                v1.append(v4)
            v5 += 1
        return v1
