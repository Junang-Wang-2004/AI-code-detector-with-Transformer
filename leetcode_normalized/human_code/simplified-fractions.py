import fractions

class C1(object):

    def simplifiedFractions(self, a1):
        """
        """
        v1 = set()
        for v2 in range(1, a1 + 1):
            for v3 in range(1, v2):
                v4 = fractions.gcd(v3, v2)
                v1.add((v3 // v4, v2 // v4))
        return ['{}/{}'.format(*x) for v5 in v1]
