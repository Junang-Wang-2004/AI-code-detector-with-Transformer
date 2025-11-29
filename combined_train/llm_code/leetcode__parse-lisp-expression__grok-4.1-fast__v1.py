class C1:

    def evaluate(self, a1):
        v1 = ['']
        v2 = {}
        v3 = []
        for v4 in a1:
            if v4 == '(':
                if v1[0] == 'let':
                    self._compute(v1, v2)
                v3.append((v1[:], v2.copy()))
                v1 = ['']
            elif v4 == ' ':
                v1.append('')
            elif v4 == ')':
                v5 = self._compute(v1, v2)
                v1, v2 = v3.pop()
                v1[-1] += v5
            else:
                v1[-1] += v4
        return int(v1[0])

    def _compute(self, a1, a2):
        v1 = a1[0]
        if v1 in ('add', 'mult'):
            v2 = [a2.get(term, term) for v3 in a1[1:]]
            v4, v5 = map(int, v2)
            return str(v4 + v5 if v1 == 'add' else v4 * v5)
        for v6 in range(1, len(a1) - 1, 2):
            v7 = a1[v6]
            v8 = a2.get(a1[v6 + 1], a1[v6 + 1])
            a2[v7] = v8
        return a2.get(a1[-1], a1[-1])
