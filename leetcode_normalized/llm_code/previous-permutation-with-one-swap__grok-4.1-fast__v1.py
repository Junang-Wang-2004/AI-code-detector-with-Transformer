class C1:

    def prevPermOpt1(self, a1):
        v1 = len(a1)
        v2 = v1 - 2
        while v2 >= 0:
            if a1[v2] > a1[v2 + 1]:
                break
            v2 -= 1
        else:
            return a1
        v3 = v1 - 1
        while a1[v3] >= a1[v2]:
            v3 -= 1
        while v3 > 0 and a1[v3 - 1] == a1[v3]:
            v3 -= 1
        a1[v2], a1[v3] = (a1[v3], a1[v2])
        return a1
