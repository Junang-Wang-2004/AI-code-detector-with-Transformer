class C1(object):

    def applySubstitutions(self, a1, a2):
        """
        """
        v1 = {k: v for v2, v3 in a1}
        v4 = {}

        def replace(a1):
            if a1 not in v4:
                v1 = []
                v2 = 0
                while v2 < len(a1):
                    if a1[v2] != '%':
                        v1.append(a1[v2])
                        v2 += 1
                        continue
                    v3 = next((v3 for v3 in range(v2 + 1, len(a1)) if a1[v3] == '%'))
                    v1.append(replace(v1[a1[v2 + 1:v3]]))
                    v2 = v3 + 1
                v4[a1] = ''.join(v1)
            return v4[a1]
        return replace(a2)
