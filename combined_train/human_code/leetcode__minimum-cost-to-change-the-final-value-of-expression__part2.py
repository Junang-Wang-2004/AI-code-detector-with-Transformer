class C1(object):

    def minOperationsToFlip(self, a1):
        """
        """
        v1 = [[None] * 3]
        for v2 in a1:
            if v2 == '(':
                v1.append([None] * 3)
            elif v2 in {')', '0', '1'}:
                if v2 == ')':
                    v3, v4, v5 = v1.pop()
                else:
                    v3, v4 = (int(v2 != '0'), int(v2 != '1'))
                if v1[-1][2] == '&':
                    v1[-1] = [min(v1[-1][0], v3), min(v1[-1][1] + v4, min(v1[-1][1], v4) + 1), None]
                elif v1[-1][2] == '|':
                    v1[-1] = [min(v1[-1][0] + v3, min(v1[-1][0], v3) + 1), min(v1[-1][1], v4), None]
                else:
                    v1[-1] = [v3, v4, None]
            else:
                v1[-1][2] = v2
        return max(v1[0][0], v1[0][1])
