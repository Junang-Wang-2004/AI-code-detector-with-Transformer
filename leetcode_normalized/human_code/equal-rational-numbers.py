from fractions import Fraction

class C1(object):

    def isRationalEqual(self, a1, a2):
        """
        """

        def frac(a1):
            if '.' not in a1:
                return Fraction(int(a1), 1)
            v1 = a1.index('.')
            v2 = Fraction(int(a1[:v1]), 1)
            v3 = a1[v1 + 1:]
            if '(' not in v3:
                if v3:
                    v2 += Fraction(int(v3), 10 ** len(v3))
                return v2
            v1 = v3.index('(')
            if v1:
                v2 += Fraction(int(v3[:v1]), 10 ** v1)
            v4 = v3[v1 + 1:-1]
            v2 += Fraction(int(v4), 10 ** v1 * (10 ** len(v4) - 1))
            return v2
        return frac(a1) == frac(a2)
