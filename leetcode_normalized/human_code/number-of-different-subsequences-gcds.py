import fractions

class C1(object):

    def countDifferentSubsequenceGCDs(self, a1):
        """
        """
        v1, v2 = (max(a1), set(a1))
        v3 = 0
        for v4 in range(1, v1 + 1):
            v5 = 0
            for v6 in range(v4, v1 + 1, v4):
                if v6 not in v2:
                    continue
                v5 = fractions.gcd(v5, v6)
                if v5 == v4:
                    v3 += 1
                    break
        return v3
