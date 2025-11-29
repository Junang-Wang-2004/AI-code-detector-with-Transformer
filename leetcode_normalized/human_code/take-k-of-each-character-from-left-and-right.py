class C1(object):

    def takeCharacters(self, a1, a2):
        """
        """
        v1 = [0] * 3
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        if min(v1) < a2:
            return -1
        v3 = v4 = 0
        for v5 in range(len(a1)):
            v1[ord(a1[v5]) - ord('a')] -= 1
            while v1[ord(a1[v5]) - ord('a')] < a2:
                v1[ord(a1[v4]) - ord('a')] += 1
                v4 += 1
            v3 = max(v3, v5 - v4 + 1)
        return len(a1) - v3
