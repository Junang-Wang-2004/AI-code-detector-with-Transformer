class C1(object):

    def reverseParentheses(self, a1):
        """
        """
        v1, v2 = ([], {})
        for v3, v4 in enumerate(a1):
            if v4 == '(':
                v1.append(v3)
            elif v4 == ')':
                v5 = v1.pop()
                v2[v3], v2[v5] = (v5, v3)
        v6 = []
        v3, v7 = (0, 1)
        while v3 < len(a1):
            if v3 in v2:
                v3 = v2[v3]
                v7 *= -1
            else:
                v6.append(a1[v3])
            v3 += v7
        return ''.join(v6)
