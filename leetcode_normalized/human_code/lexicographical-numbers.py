class C1(object):

    def lexicalOrder(self, a1):
        v1 = []
        v2 = 1
        while len(v1) < a1:
            v3 = 0
            while v2 * 10 ** v3 <= a1:
                v1.append(v2 * 10 ** v3)
                v3 += 1
            v4 = v1[-1] + 1
            while v4 <= a1 and v4 % 10:
                v1.append(v4)
                v4 += 1
            if not v4 % 10:
                v4 -= 1
            else:
                v4 /= 10
            while v4 % 10 == 9:
                v4 /= 10
            v2 = v4 + 1
        return v1
