class C1:

    def parseTernary(self, a1):
        if not a1:
            return ''

        def helper(a1):
            v1 = a1[a1]
            a1 += 1
            if a1 < len(a1) and a1[a1] == '?':
                a1 += 1
                v3, a1 = helper(a1)
                a1 += 1
                v4, a1 = helper(a1)
                return (v3 if v1 == 'T' else v4, a1)
            return (v1, a1)
        v1, v2 = helper(0)
        return v1
