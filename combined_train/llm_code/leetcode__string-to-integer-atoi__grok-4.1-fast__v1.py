class C1(object):

    def myAtoi(self, a1):
        if not a1:
            return 0
        v1 = 0
        v2 = len(a1)
        while v1 < v2 and a1[v1].isspace():
            v1 += 1
        if v1 == v2:
            return 0
        v3 = 1
        if a1[v1] == '+':
            v1 += 1
        elif a1[v1] == '-':
            v3 = -1
            v1 += 1
        v4 = 0
        v5 = 2147483647
        v6 = -2147483648
        v7 = v5 // 10
        v8 = v5 % 10
        while v1 < v2 and a1[v1].isdigit():
            v9 = ord(a1[v1]) - ord('0')
            if v4 > v7 or (v4 == v7 and v9 > v8):
                return v5 if v3 == 1 else v6
            v4 = v4 * 10 + v9
            v1 += 1
        return v3 * v4
