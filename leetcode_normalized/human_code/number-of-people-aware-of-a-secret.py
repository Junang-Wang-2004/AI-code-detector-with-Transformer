class C1(object):

    def peopleAwareOfSecret(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [0] * a3
        v2[0] = 1
        for v3 in range(1, a1):
            v2[v3 % a3] = ((v2[(v3 - 1) % a3] if v3 - 1 else 0) - v2[v3 % a3] + v2[(v3 - a2) % a3]) % v1
        return sum(v2) % v1
