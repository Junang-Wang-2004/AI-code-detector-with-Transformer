class C1(object):

    def isAdditiveNumber(self, a1):
        """
        """

        def add(a1, a2):
            v1, v2, v3 = ('', 0, 0)
            for v4 in range(max(len(a1), len(a2))):
                v3 = v2
                if v4 < len(a1):
                    v3 += int(a1[-(v4 + 1)])
                if v4 < len(a2):
                    v3 += int(a2[-(v4 + 1)])
                v2, v3 = (v3 / 10, v3 % 10)
                v1 += str(v3)
            if v2:
                v1 += str(v2)
            return v1[::-1]
        for v1 in range(1, len(a1)):
            for v2 in range(v1 + 1, len(a1)):
                v3, v4 = (a1[0:v1], a1[v1:v2])
                if len(v3) > 1 and v3[0] == '0' or (len(v4) > 1 and v4[0] == '0'):
                    continue
                v5 = add(v3, v4)
                v6 = v3 + v4 + v5
                while len(v6) < len(a1):
                    v3, v4, v5 = (v4, v5, add(v4, v5))
                    v6 += v5
                if v6 == a1:
                    return True
        return False
