class C1(object):

    def gcdOfStrings(self, a1, a2):
        """
        """

        def check(a1, a2):
            v1 = 0
            for v2 in a1:
                if v2 != a2[v1]:
                    return False
                v1 = (v1 + 1) % len(a2)
            return True

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        if not a1 or not a2:
            return ''
        v1 = gcd(len(a1), len(a2))
        v2 = a1[:v1]
        return v2 if check(a1, v2) and check(a2, v2) else ''
