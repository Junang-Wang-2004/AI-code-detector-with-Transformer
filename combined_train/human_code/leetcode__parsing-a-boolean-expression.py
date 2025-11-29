class C1(object):

    def parseBoolExpr(self, a1):
        """
        """

        def parse(a1, a2):
            if a1[a2[0]] not in '&|!':
                v1 = a1[a2[0]] == 't'
                a2[0] += 1
                return v1
            v2 = a1[a2[0]]
            a2[0] += 2
            v3 = []
            while a1[a2[0]] != ')':
                if a1[a2[0]] == ',':
                    a2[0] += 1
                    continue
                v3.append(parse(a1, a2))
            a2[0] += 1
            if v2 == '&':
                return all(v3)
            if v2 == '|':
                return any(v3)
            return not v3[0]
        return parse(a1, [0])
