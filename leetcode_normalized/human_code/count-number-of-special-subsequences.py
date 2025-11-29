class C1(object):

    def countSpecialSubsequences(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * 3
        for v3 in a1:
            v2[v3] = ((v2[v3] + v2[v3]) % v1 + (v2[v3 - 1] if v3 - 1 >= 0 else 1)) % v1
        return v2[-1]
