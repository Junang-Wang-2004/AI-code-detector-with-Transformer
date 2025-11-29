class C1(object):

    def reverseParentheses(self, a1):
        v1 = []
        for v2 in a1:
            if v2 == ')':
                v3 = []
                while v1 and v1[-1] != '(':
                    v3.append(v1.pop())
                v1.pop()
                v1.extend(v3)
            else:
                v1.append(v2)
        return ''.join(v1)
