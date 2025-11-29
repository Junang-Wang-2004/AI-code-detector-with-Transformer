class C1:

    def gcdOfStrings(self, a1, a2):
        if not a1 or not a2:
            return ''

        def find_gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = find_gcd(len(a1), len(a2))
        if a1 + a2 == a2 + a1:
            return a1[:v1]
        return ''
