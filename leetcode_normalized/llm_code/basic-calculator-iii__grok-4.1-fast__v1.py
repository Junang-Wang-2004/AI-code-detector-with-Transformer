class C1(object):

    def calculate(self, a1):

        def expr(a1):
            v1 = term(a1)
            while a1[0] < len(a1) and a1[a1[0]] in '+-':
                v2 = a1[a1[0]]
                a1[0] += 1
                v3 = term(a1)
                v1 += v3 if v2 == '+' else v1 - v3
            return v1

        def term(a1):
            v1 = factor(a1)
            while a1[0] < len(a1) and a1[a1[0]] in '*/':
                v2 = a1[a1[0]]
                a1[0] += 1
                v3 = factor(a1)
                v1 = v1 * v3 if v2 == '*' else int(v1 / v3)
            return v1

        def factor(a1):
            if a1[a1[0]].isdigit():
                v1 = 0
                while a1[0] < len(a1) and a1[a1[0]].isdigit():
                    v1 = v1 * 10 + int(a1[a1[0]])
                    a1[0] += 1
                return v1
            a1[0] += 1
            v2 = expr(a1)
            a1[0] += 1
            return v2
        v1 = [0]
        return expr(v1)
