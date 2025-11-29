class C1(object):

    def minimumBoxes(self, a1):
        v1 = 0
        v2 = 0
        while True:
            v3 = v2 + (v1 + 1) * (v1 + 2) // 2
            if v3 > a1:
                break
            v2 = v3
            v1 += 1
        v4 = a1 - v2
        v5 = 0
        v6 = 0
        while v6 < v4:
            v5 += 1
            v6 = v5 * (v5 + 1) // 2
        v7 = v1 * (v1 + 1) // 2 + v5
        return v7
