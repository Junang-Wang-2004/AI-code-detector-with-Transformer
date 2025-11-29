class C1(object):

    def generateParenthesis(self, a1):
        """
        """
        v1, v2 = ([], [])
        v3 = [(1, (a1, a1))]
        while v3:
            v4, v5 = v3.pop()
            if v4 == 1:
                v6, v7 = v5
                if v6 == 0 and v7 == 0:
                    v1.append(''.join(v2))
                if v6 < v7:
                    v3.append((3, tuple()))
                    v3.append((1, (v6, v7 - 1)))
                    v3.append((2, ')'))
                if v6 > 0:
                    v3.append((3, tuple()))
                    v3.append((1, (v6 - 1, v7)))
                    v3.append((2, '('))
            elif v4 == 2:
                v2.append(v5[0])
            elif v4 == 3:
                v2.pop()
        return v1
