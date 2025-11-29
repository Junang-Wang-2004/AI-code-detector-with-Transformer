class C1:

    def scoreOfParentheses(self, a1):
        v1 = []
        v2 = 0
        for v3, v4 in enumerate(a1):
            if v4 == '(':
                v1.append(v3)
            else:
                v5 = v1.pop()
                if v3 - v5 == 1:
                    v2 += 1 << len(v1)
        return v2
