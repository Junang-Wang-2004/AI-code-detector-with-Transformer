class C1(object):

    def calculate(self, a1):
        v1, v2 = ([], [])
        v3 = ''
        for v4 in reversed(range(len(a1))):
            if a1[v4].isdigit():
                v3 += a1[v4]
                if v4 == 0 or not a1[v4 - 1].isdigit():
                    v1.append(int(v3[::-1]))
                    v3 = ''
            elif a1[v4] == ')' or a1[v4] == '+' or a1[v4] == '-':
                v2.append(a1[v4])
            elif a1[v4] == '(':
                while v2[-1] != ')':
                    self.compute(v1, v2)
                v2.pop()
        while v2:
            self.compute(v1, v2)
        return v1[-1]

    def compute(self, a1, a2):
        v1, v2 = (a1.pop(), a1.pop())
        v3 = a2.pop()
        if v3 == '+':
            a1.append(v1 + v2)
        elif v3 == '-':
            a1.append(v1 - v2)
