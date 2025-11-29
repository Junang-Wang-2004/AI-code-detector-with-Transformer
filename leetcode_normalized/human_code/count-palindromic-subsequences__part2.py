class C1(object):

    def countPalindromes(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        for v3 in range(10):
            for v4 in range(10):
                v5 = '%s%s*%s%s' % (v3, v4, v4, v3)
                v6 = [0] * (5 + 1)
                v6[0] = 1
                for v7 in range(len(a1)):
                    for v8 in reversed(range(5)):
                        if v5[v8] == '*' or v5[v8] == a1[v7]:
                            v6[v8 + 1] = (v6[v8 + 1] + v6[v8]) % v1
                v2 = (v2 + v6[5]) % v1
        return v2
