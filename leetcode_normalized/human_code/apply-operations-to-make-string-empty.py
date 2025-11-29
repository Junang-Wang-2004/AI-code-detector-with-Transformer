class C1(object):

    def lastNonEmptyString(self, a1):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        v3 = max(v1)
        v4 = []
        for v2 in reversed(a1):
            if v1[ord(v2) - ord('a')] != v3:
                continue
            v1[ord(v2) - ord('a')] -= 1
            v4.append(v2)
        return ''.join(reversed(v4))
