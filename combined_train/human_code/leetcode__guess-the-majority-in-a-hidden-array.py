class C1(object):

    def query(self, a1, a2, a3, a4):
        """
        """
        pass

    def length(self):
        """
        """
        pass

class C2(object):

    def guessMajority(self, a1):
        """
        """
        v1, v2, v3 = (1, 0, None)
        v4 = a1.query(0, 1, 2, 3)
        for v5 in reversed(range(4, a1.length())):
            v6 = a1.query(0, 1, 2, v5)
            if v6 == v4:
                v1 = v1 + 1
            else:
                v2, v3 = (v2 + 1, v5)
        v7 = v6
        for v5 in range(3):
            v8 = a1.query(*[v for v9 in [0, 1, 2, 3, 4] if v9 != v5])
            if v8 == v7:
                v1 = v1 + 1
            else:
                v2, v3 = (v2 + 1, v5)
        if v1 == v2:
            return -1
        return 3 if v1 > v2 else v3
