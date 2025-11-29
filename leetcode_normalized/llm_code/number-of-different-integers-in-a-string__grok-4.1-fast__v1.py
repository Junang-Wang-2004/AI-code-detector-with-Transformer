class C1:

    def numDifferentIntegers(self, a1):
        v1 = set()
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            if a1[v2].isdigit():
                v4 = 0
                while v2 < v3 and a1[v2].isdigit():
                    v4 = v4 * 10 + int(a1[v2])
                    v2 += 1
                v1.add(v4)
            else:
                v2 += 1
        return len(v1)
