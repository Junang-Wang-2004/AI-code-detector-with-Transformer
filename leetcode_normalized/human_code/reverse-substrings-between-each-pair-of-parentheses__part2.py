class C1(object):

    def reverseParentheses(self, a1):
        """
        """
        v1 = [[]]
        for v2 in a1:
            if v2 == '(':
                v1.append([])
            elif v2 == ')':
                v3 = v1.pop()
                v3.reverse()
                v1[-1].extend(v3)
            else:
                v1[-1].append(v2)
        return ''.join(v1.pop())
