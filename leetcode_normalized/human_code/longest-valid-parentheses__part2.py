class C1(object):

    def longestValidParentheses(self, a1):
        v1, v2, v3 = (0, -1, [])
        for v4 in range(len(a1)):
            if a1[v4] == '(':
                v3.append(v4)
            elif not v3:
                v2 = v4
            else:
                v3.pop()
                if not v3:
                    v1 = max(v1, v4 - v2)
                else:
                    v1 = max(v1, v4 - v3[-1])
        return v1
