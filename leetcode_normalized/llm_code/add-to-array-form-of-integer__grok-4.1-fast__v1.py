class C1(object):

    def addToArrayForm(self, a1, a2):
        v1 = []
        v2 = len(a1) - 1
        while v2 >= 0 or a2 > 0:
            if v2 >= 0:
                v3 = a1[v2] + a2 % 10
                a2 //= 10
            else:
                v3 = a2 % 10
                a2 //= 10
            v1.append(v3 % 10)
            a2 += v3 // 10
            if v2 >= 0:
                v2 -= 1
        v1.reverse()
        return v1
