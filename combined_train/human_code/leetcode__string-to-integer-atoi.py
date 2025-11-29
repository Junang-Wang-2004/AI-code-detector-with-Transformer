class C1(object):

    def myAtoi(self, a1):
        """
        """
        v1 = 2147483647
        v2 = -2147483648
        v3 = 0
        if not a1:
            return v3
        v4 = 0
        while v4 < len(a1) and a1[v4].isspace():
            v4 += 1
        if len(a1) == v4:
            return v3
        v5 = 1
        if a1[v4] == '+':
            v4 += 1
        elif a1[v4] == '-':
            v5 = -1
            v4 += 1
        while v4 < len(a1) and '0' <= a1[v4] <= '9':
            if v3 > (v1 - int(a1[v4])) / 10:
                return v1 if v5 > 0 else v2
            v3 = v3 * 10 + int(a1[v4])
            v4 += 1
        return v5 * v3
