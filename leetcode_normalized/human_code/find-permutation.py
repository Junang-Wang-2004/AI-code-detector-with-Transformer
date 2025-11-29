class C1(object):

    def findPermutation(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1) + 1):
            if v2 == len(a1) or a1[v2] == 'I':
                v1 += list(range(v2 + 1, len(v1), -1))
        return v1
