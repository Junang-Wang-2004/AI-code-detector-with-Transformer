class C1(object):

    def evaluateExpression(self, a1):
        """
        """
        v1 = {'add': lambda a, b: a + b, 'sub': lambda a, b: a - b, 'mul': lambda a, b: a * b, 'div': lambda a, b: a // b}
        v2 = '(,)'
        v3, v4 = ([[]], [])
        for v5 in a1:
            if v5 not in v2:
                v4.append(v5)
                continue
            if v5 == '(':
                v3.append([''.join(v4)])
                v4 = []
                continue
            if v4:
                v3[-1].append(int(''.join(v4)))
                v4 = []
            if v5 != ')':
                continue
            v6, v7, v8 = v3.pop()
            v3[-1].append(v1[v6](v7, v8))
        return v3[0][0] if v3[0] else int(''.join(v4))
