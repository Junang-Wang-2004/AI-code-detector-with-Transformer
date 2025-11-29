class C1:

    def applySubstitutions(self, a1, a2):
        v1 = dict(a1)
        v2 = {}

        def substitute(a1):
            if a1 in v2:
                return v2[a1]
            v1 = []
            v2 = 0
            while v2 < len(a1):
                v3 = a1.find('%', v2)
                if v3 == -1:
                    v1.append(a1[v2:])
                    break
                if v3 > v2:
                    v1.append(a1[v2:v3])
                v2 = v3
                v4 = a1.find('%', v2 + 1)
                if v4 == -1:
                    v1.append(a1[v2:])
                    break
                v5 = a1[v2 + 1:v4]
                v1.append(substitute(v1[v5]))
                v2 = v4 + 1
            v6 = ''.join(v1)
            v2[a1] = v6
            return v6
        return substitute(a2)
