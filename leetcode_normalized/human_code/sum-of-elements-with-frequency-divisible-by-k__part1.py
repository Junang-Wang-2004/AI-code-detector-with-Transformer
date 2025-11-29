class C1(object):

    def sumDivisibleByK(self, a1, a2):
        """
        """
        v1 = max(a1)
        v2 = [0] * (v1 + 1)
        for v3 in a1:
            v2[v3] += 1
        return sum((v3 for v3 in a1 if v2[v3] % a2 == 0))
