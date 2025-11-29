class C1(object):

    def canConstruct(self, a1, a2):
        """
        """
        v1 = [0] * 26
        v2 = 0
        for v3 in a1:
            if v1[ord(v3) - ord('a')] == 0:
                v2 += 1
            v1[ord(v3) - ord('a')] += 1
        for v3 in a2:
            v1[ord(v3) - ord('a')] -= 1
            if v1[ord(v3) - ord('a')] == 0:
                v2 -= 1
                if v2 == 0:
                    break
        return v2 == 0
