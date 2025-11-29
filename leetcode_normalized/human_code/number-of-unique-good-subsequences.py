class C1(object):

    def numberOfUniqueGoodSubsequences(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 0)
        v4 = False
        for v5 in a1:
            if v5 == '1':
                v3 = (v2 + v3 + 1) % v1
            else:
                v2 = (v2 + v3) % v1
                v4 = True
        return (v2 + v3 + int(v4)) % v1
