class C1(object):

    def scoreOfParentheses(self, a1):
        """
        """
        v1 = [0]
        for v2 in a1:
            if v2 == '(':
                v1.append(0)
            else:
                v3 = v1.pop()
                v1[-1] += max(1, 2 * v3)
        return v1[0]
