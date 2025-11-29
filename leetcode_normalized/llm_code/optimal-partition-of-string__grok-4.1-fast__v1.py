class C1:

    def partitionString(self, a1):
        v1 = 1
        v2 = set()
        for v3 in a1:
            if v3 in v2:
                v1 += 1
                v2.clear()
                v2.add(v3)
            else:
                v2.add(v3)
        return v1
