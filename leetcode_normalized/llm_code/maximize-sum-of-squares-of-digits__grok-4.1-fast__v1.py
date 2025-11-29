class C1(object):

    def maxSumOfSquares(self, a1, a2):
        if a2 > 9 * a1:
            return ''
        v1 = a2 // 9
        v2 = a2 % 9
        v3 = a1 - v1 - (1 if v2 > 0 else 0)
        v4 = '9' * v1
        v5 = str(v2) if v2 > 0 else ''
        v6 = '0' * v3
        return v4 + v5 + v6
