class C1:

    def findRepeatedDnaSequences(self, a1):
        v1 = set()
        v2 = set()
        for v3 in range(len(a1) - 9):
            v4 = a1[v3:v3 + 10]
            if v4 in v1:
                v2.add(v4)
            v1.add(v4)
        return list(v2)
