class C1:

    def parseBoolExpr(self, a1):

        def evaluate(a1):
            v1 = a1[a1]
            if v1 == 't':
                return (True, a1 + 1)
            if v1 == 'f':
                return (False, a1 + 1)
            v2 = v1
            a1 += 2
            v4 = []
            while a1[a1] != ')':
                if a1[a1] == ',':
                    a1 += 1
                    continue
                v5, a1 = evaluate(a1)
                v4.append(v5)
            a1 += 1
            if v2 == '&':
                return (all(v4), a1)
            if v2 == '|':
                return (any(v4), a1)
            return (not v4[0], a1)
        return evaluate(0)[0]
