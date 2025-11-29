class C1:

    def longestValidParentheses(self, a1):
        v1 = [-1]
        v2 = 0
        for v3 in range(len(a1)):
            if a1[v3] == '(':
                v1.append(v3)
            else:
                v1.pop()
                if v1:
                    v2 = max(v2, v3 - v1[-1])
                else:
                    v1.append(v3)
        return v2
