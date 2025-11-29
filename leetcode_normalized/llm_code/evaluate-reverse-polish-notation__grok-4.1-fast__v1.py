class C1:

    def evalRPN(self, a1):
        v1 = []
        for v2 in a1:
            try:
                v1.append(int(v2))
            except ValueError:
                v3 = v1.pop()
                v4 = v1.pop()
                if v2 == '+':
                    v1.append(v4 + v3)
                elif v2 == '-':
                    v1.append(v4 - v3)
                elif v2 == '*':
                    v1.append(v4 * v3)
                else:
                    v1.append(int(v4 / v3))
        return v1.pop()
