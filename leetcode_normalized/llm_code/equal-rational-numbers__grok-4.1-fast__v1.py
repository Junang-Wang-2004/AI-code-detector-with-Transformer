class C1(object):

    def isRationalEqual(self, a1, a2):

        def to_fraction(a1):
            if '.' not in a1:
                return (int(a1), 1)
            v1, v2 = a1.split('.')
            v3 = int(v1) if v1 else 0
            if '(' not in v2:
                v4 = len(v2)
                v5 = int(v2) if v2 else 0
                v6 = 10 ** v4
            else:
                v7 = v2.index('(')
                v8 = v2[:v7]
                v9 = len(v8)
                v10 = v2.index(')', v7)
                v11 = v2[v7 + 1:v10]
                v12 = len(v11)
                v13 = int(v8) if v8 else 0
                v14 = int(v11)
                v15 = 10 ** v12 - 1
                v5 = v13 * v15 + v14
                v6 = 10 ** v9 * v15
            return (v3 * v6 + v5, v6)
        v1, v2 = to_fraction(a1)
        v3, v4 = to_fraction(a2)
        return v1 * v4 == v3 * v2
