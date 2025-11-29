class C1:

    def evaluate(self, a1, a2):
        v1 = dict(a2)
        v2 = []
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            if a1[v3] == '(':
                v5 = v3 + 1
                while a1[v5] != ')':
                    v5 += 1
                v6 = a1[v3 + 1:v5]
                v2.append(v1.get(v6, '?'))
                v3 = v5 + 1
            else:
                v2.append(a1[v3])
                v3 += 1
        return ''.join(v2)
