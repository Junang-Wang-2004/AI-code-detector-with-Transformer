class C1:

    def addStrings(self, a1, a2):
        if len(a1) < len(a2):
            a1 = '0' * (len(a2) - len(a1)) + a1
        else:
            a2 = '0' * (len(a1) - len(a2)) + a2
        v3 = ''
        v4 = 0
        for v5, v6 in zip(reversed(a1), reversed(a2)):
            v7 = int(v5) + int(v6) + v4
            v3 = str(v7 % 10) + v3
            v4 = v7 // 10
        while v4:
            v3 = str(v4 % 10) + v3
            v4 //= 10
        return v3
