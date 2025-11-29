class C1(object):

    def calPoints(self, a1):
        """
        """
        v1 = []
        for v2 in a1:
            if v2 == '+':
                v1.append(v1[-1] + v1[-2])
            elif v2 == 'D':
                v1.append(v1[-1] * 2)
            elif v2 == 'C':
                v1.pop()
            else:
                v1.append(int(v2))
        return sum(v1)
