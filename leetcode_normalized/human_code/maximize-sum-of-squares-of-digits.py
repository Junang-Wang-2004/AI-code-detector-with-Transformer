class C1(object):

    def maxSumOfSquares(self, a1, a2):
        """
        """
        if a1 * 9 < a2:
            return ''
        v1, v2 = divmod(a2, 9)
        v3 = ['0'] * a1
        for v4 in range(v1):
            v3[v4] = '9'
        if v2:
            v3[v1] = str(v2)
        return ''.join(v3)
