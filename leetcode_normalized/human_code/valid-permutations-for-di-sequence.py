class C1(object):

    def numPermsDISequence(self, a1):
        """
        """
        v1 = [1] * (len(a1) + 1)
        for v2 in a1:
            if v2 == 'I':
                v1 = v1[:-1]
                for v3 in range(1, len(v1)):
                    v1[v3] += v1[v3 - 1]
            else:
                v1 = v1[1:]
                for v3 in reversed(range(len(v1) - 1)):
                    v1[v3] += v1[v3 + 1]
        return v1[0] % (10 ** 9 + 7)
