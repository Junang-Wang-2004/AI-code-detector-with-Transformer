import operator

class C1(object):

    def evalRPN(self, a1):
        v1, v2 = ([], {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div})
        for v3 in a1:
            if v3 not in v2:
                v1.append(int(v3))
            else:
                v4, v5 = (v1.pop(), v1.pop())
                v1.append(int(v2[v3](v5 * 1.0, v4)))
        return v1.pop()
