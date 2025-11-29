class C1(object):

    def fractionToDecimal(self, a1, a2):
        """
        """
        v1 = ''
        if a1 > 0 and a2 < 0 or (a1 < 0 and a2 > 0):
            v1 = '-'
        v2, v3 = (abs(a1), abs(a2))
        v1 += str(v2 / v3)
        v2 %= v3
        if v2 > 0:
            v1 += '.'
        v4 = {}
        while v2 and v2 not in v4:
            v4[v2] = len(v1)
            v2 *= 10
            v1 += str(v2 / v3)
            v2 %= v3
        if v2 in v4:
            v1 = v1[:v4[v2]] + '(' + v1[v4[v2]:] + ')'
        return v1
