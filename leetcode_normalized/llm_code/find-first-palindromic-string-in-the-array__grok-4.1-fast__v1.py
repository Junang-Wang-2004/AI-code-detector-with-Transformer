class C1:

    def firstPalindrome(self, a1):
        for v1 in a1:
            v2 = ''
            for v3 in v1:
                v2 = v3 + v2
            if v1 == v2:
                return v1
        return ''
