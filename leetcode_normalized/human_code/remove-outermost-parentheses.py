class C1(object):

    def removeOuterParentheses(self, a1):
        """
        """
        v1 = 1
        v2, v3 = ([], 0)
        for v4 in a1:
            if v4 == '(' and v3 >= v1:
                v2.append(v4)
            if v4 == ')' and v3 > v1:
                v2.append(v4)
            v3 += 1 if v4 == '(' else -1
        return ''.join(v2)
