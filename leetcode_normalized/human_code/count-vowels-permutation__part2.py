class C1(object):

    def countVowelPermutation(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4, v5, v6 = (1, 1, 1, 1, 1)
        for v7 in range(1, a1):
            v2, v3, v4, v5, v6 = ((v3 + v4 + v6) % v1, (v2 + v4) % v1, (v3 + v5) % v1, v4, (v4 + v5) % v1)
        return (v2 + v3 + v4 + v5 + v6) % v1
