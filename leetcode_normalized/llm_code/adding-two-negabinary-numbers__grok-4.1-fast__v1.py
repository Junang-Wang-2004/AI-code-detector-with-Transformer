class C1:

    def addNegabinary(self, a1, a2):
        v1 = []
        v2 = 0
        v3 = len(a1) - 1
        v4 = len(a2) - 1
        while v3 >= 0 or v4 >= 0 or v2:
            v5 = v2
            if v3 >= 0:
                v5 += a1[v3]
                v3 -= 1
            if v4 >= 0:
                v5 += a2[v4]
                v4 -= 1
            v1.append(v5 % 2)
            v2 = -(v5 // 2)
        while len(v1) > 1 and v1[-1] == 0:
            v1.pop()
        v1.reverse()
        return v1
