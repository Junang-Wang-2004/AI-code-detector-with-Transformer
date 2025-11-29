class C1(object):

    def evaluate(self, a1):
        """
        """

        def getval(a1, a2):
            return a1.get(a2, a2)

        def evaluate(a1, a2):
            if a1[0] in ('add', 'mult'):
                v1, v2 = list(map(int, [getval(a2, x) for v3 in a1[1:]]))
                return str(v1 + v2 if a1[0] == 'add' else v1 * v2)
            for v4 in range(1, len(a1) - 1, 2):
                if a1[v4 + 1]:
                    a2[a1[v4]] = getval(a2, a1[v4 + 1])
            return getval(a2, a1[-1])
        v1, v2, v3 = ([''], {}, [])
        for v4 in a1:
            if v4 == '(':
                if v1[0] == 'let':
                    evaluate(v1, v2)
                v3.append((v1, dict(v2)))
                v1 = ['']
            elif v4 == ' ':
                v1.append('')
            elif v4 == ')':
                v5 = evaluate(v1, v2)
                v1, v2 = v3.pop()
                v1[-1] += v5
            else:
                v1[-1] += v4
        return int(v1[0])
