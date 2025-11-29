class C1(object):

    def lexicalOrder(self, a1):
        v1 = []
        v2 = []
        for v3 in range(9, 0, -1):
            if v3 <= a1:
                v2.append(v3)
        while v2 and len(v1) < a1:
            v4 = v2.pop()
            v1.append(v4)
            for v5 in range(9, 0, -1):
                v6 = v4 * 10 + v5
                if v6 <= a1:
                    v2.append(v6)
            v7 = v4 * 10
            if v7 <= a1:
                v2.append(v7)
        return v1
