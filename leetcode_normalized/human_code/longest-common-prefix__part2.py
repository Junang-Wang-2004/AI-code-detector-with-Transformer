class C1(object):

    def longestCommonPrefix(self, a1):
        """
        """
        v1 = ''
        for v2 in zip(*a1):
            if all((c == v2[0] for v3 in v2)):
                v1 += v2[0]
            else:
                return v1
        return v1
