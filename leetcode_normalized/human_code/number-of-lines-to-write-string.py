class C1(object):

    def numberOfLines(self, a1, a2):
        """
        """
        v1 = [1, 0]
        for v2 in a2:
            v3 = a1[ord(v2) - ord('a')]
            v1[1] += v3
            if v1[1] > 100:
                v1[0] += 1
                v1[1] = v3
        return v1
