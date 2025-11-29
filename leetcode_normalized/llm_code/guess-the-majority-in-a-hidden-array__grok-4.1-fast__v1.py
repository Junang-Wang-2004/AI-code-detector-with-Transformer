class C1(object):

    def query(self, a1, a2, a3, a4):
        pass

    def length(self):
        pass

class C2(object):

    def guessMajority(self, a1):
        v1 = a1.query(0, 1, 2, 3)
        v2 = a1.query(0, 1, 2, 4)
        v3 = 1
        v4 = 0
        v5 = None
        v6 = a1.length()
        if v2 == v1:
            v3 += 1
        else:
            v4 += 1
            v5 = 4
        for v7 in range(5, v6):
            v8 = a1.query(0, 1, 2, v7)
            if v8 == v1:
                v3 += 1
            else:
                v4 += 1
                v5 = v7
        v9 = a1.query(1, 2, 3, 4)
        if v9 == v2:
            v3 += 1
        else:
            v4 += 1
            v5 = 0
        v10 = a1.query(0, 2, 3, 4)
        if v10 == v2:
            v3 += 1
        else:
            v4 += 1
            v5 = 1
        v11 = a1.query(0, 1, 3, 4)
        if v11 == v2:
            v3 += 1
        else:
            v4 += 1
            v5 = 2
        if v3 == v4:
            return -1
        return 3 if v3 > v4 else v5
