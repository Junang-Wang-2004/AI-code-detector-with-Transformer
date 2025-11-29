class C1:

    def calculate(self, a1):
        v1 = [0]

        def factor():
            if a1[v1[0]].isdigit():
                v1 = 0
                while v1[0] < len(a1) and a1[v1[0]].isdigit():
                    v1 = v1 * 10 + int(a1[v1[0]])
                    v1[0] += 1
                return v1
            v1[0] += 1
            v2 = expr()
            v1[0] += 1
            return v2

        def term():
            v1 = factor()
            while v1[0] < len(a1) and a1[v1[0]] in '*/':
                v2 = a1[v1[0]]
                v1[0] += 1
                v3 = factor()
                if v2 == '*':
                    v1 *= v3
                else:
                    v1 //= v3
            return v1

        def expr():
            v1 = term()
            while v1[0] < len(a1) and a1[v1[0]] in '+-':
                v2 = a1[v1[0]]
                v1[0] += 1
                v3 = term()
                if v2 == '+':
                    v1 += v3
                else:
                    v1 -= v3
            return v1
        return expr()
