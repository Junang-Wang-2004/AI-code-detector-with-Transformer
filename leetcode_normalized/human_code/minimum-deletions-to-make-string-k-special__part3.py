class C1(object):

    def minimumDeletions(self, a1, a2):
        """
        """
        v1 = [0] * 26
        for v2 in a1:
            v1[ord(v2) - ord('a')] += 1
        return min((sum((y if y < v2 else max(y - (v2 + a2), 0) for v3 in v1 if v3)) for v2 in v1 if v2))
