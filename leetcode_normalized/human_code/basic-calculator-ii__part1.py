import operator

class C1(object):

    def calculate(self, a1):
        """
        """

        def compute(a1, a2):
            v1, v2 = (a1.pop(), a1.pop())
            a1.append(ops[a2.pop()](v2, v1))
        v1 = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        v2 = {'+': 0, '-': 0, '*': 1, '/': 1}
        v3, v4, v5 = ([], [], 0)
        for v6 in range(len(a1)):
            if a1[v6].isdigit():
                v5 = v5 * 10 + int(a1[v6])
                if v6 == len(a1) - 1 or not a1[v6 + 1].isdigit():
                    v3.append(v5)
                    v5 = 0
            elif a1[v6] == '(':
                v4.append(a1[v6])
            elif a1[v6] == ')':
                while v4[-1] != '(':
                    compute(v3, v4)
                v4.pop()
            elif a1[v6] in v2:
                while v4 and v4[-1] in v2 and (v2[v4[-1]] >= v2[a1[v6]]):
                    compute(v3, v4)
                v4.append(a1[v6])
        while v4:
            compute(v3, v4)
        return v3[-1]
