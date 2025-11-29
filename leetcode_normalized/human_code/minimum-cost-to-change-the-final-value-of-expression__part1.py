class C1(object):

    def minOperationsToFlip(self, a1):
        """
        """

        def compute(a1, a2):
            v1, v2 = (a1.pop(), a1.pop())
            a1.append(ops[a2.pop()](v2, v1))
        v1 = {'&': lambda x, y: [min(x[0], y[0]), min(x[1] + y[1], min(x[1], y[1]) + 1)], '|': lambda x, y: [min(x[0] + y[0], min(x[0], y[0]) + 1), min(x[1], y[1])]}
        v2 = {'&': 0, '|': 0}
        v3, v4 = ([], [])
        for v5 in a1:
            if v5.isdigit():
                v3.append([int(v5 != '0'), int(v5 != '1')])
            elif v5 == '(':
                v4.append(v5)
            elif v5 == ')':
                while v4[-1] != '(':
                    compute(v3, v4)
                v4.pop()
            elif v5 in v2:
                while v4 and v4[-1] in v2 and (v2[v4[-1]] >= v2[v5]):
                    compute(v3, v4)
                v4.append(v5)
        while v4:
            compute(v3, v4)
        return max(v3[-1])
