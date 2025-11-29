class C1(object):

    def scoreOfParentheses(self, a1):
        """
        """
        v1, v2 = (0, 0)
        for v3 in range(len(a1)):
            if a1[v3] == '(':
                v2 += 1
            else:
                v2 -= 1
                if a1[v3 - 1] == '(':
                    v1 += 2 ** v2
        return v1
