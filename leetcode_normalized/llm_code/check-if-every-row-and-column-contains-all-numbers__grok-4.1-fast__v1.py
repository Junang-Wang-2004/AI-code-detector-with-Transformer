class C1:

    def checkValid(self, a1):
        v1 = len(a1)
        for v2 in range(v1):
            v3 = set()
            for v4 in range(v1):
                v5 = a1[v2][v4]
                if v5 in v3:
                    return False
                v3.add(v5)
        for v4 in range(v1):
            v3 = set()
            for v2 in range(v1):
                v5 = a1[v2][v4]
                if v5 in v3:
                    return False
                v3.add(v5)
        return True
