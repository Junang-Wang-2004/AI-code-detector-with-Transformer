class C1(object):
    v1 = 0
    v2 = 1
    v3 = 2
    v4 = 3
    v5 = 4
    v6 = 5

class C2(object):

    def isNumber(self, a1):
        """
        """
        v1 = [[-1, 0, 3, 1, 2, -1], [-1, 8, -1, 1, 4, 5], [-1, -1, -1, 4, -1, -1], [-1, -1, -1, 1, 2, -1], [-1, 8, -1, 4, -1, 5], [-1, -1, 6, 7, -1, -1], [-1, -1, -1, 7, -1, -1], [-1, 8, -1, 7, -1, -1], [-1, 8, -1, -1, -1, -1]]
        v2 = 0
        for v3 in a1:
            v4 = C1.INVALID
            if v3.isspace():
                v4 = C1.SPACE
            elif v3 == '+' or v3 == '-':
                v4 = C1.SIGN
            elif v3.isdigit():
                v4 = C1.DIGIT
            elif v3 == '.':
                v4 = C1.DOT
            elif v3 == 'e' or v3 == 'E':
                v4 = C1.EXPONENT
            v2 = v1[v2][v4]
            if v2 == -1:
                return False
        return v2 == 1 or v2 == 4 or v2 == 7 or (v2 == 8)
