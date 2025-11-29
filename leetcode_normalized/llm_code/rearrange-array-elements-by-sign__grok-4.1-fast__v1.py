class C1:

    def rearrangeArray(self, a1):
        v1 = []
        v2 = []
        for v3 in a1:
            if v3 > 0:
                v1.append(v3)
            else:
                v2.append(v3)
        v4 = []
        for v5, v6 in zip(v1, v2):
            v4.extend([v5, v6])
        return v4
