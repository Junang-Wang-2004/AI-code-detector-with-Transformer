class C1:

    def removeOuterParentheses(self, a1):
        v1 = []
        v2 = 0
        for v3 in a1:
            if v3 == '(':
                v2 += 1
                if v2 > 1:
                    v1.append(v3)
            else:
                if v2 > 1:
                    v1.append(v3)
                v2 -= 1
        return ''.join(v1)
