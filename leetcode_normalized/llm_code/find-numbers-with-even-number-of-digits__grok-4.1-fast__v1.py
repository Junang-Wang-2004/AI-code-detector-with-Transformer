class C1:

    def findNumbers(self, a1):
        v1 = 0
        for v2 in a1:
            if 10 <= v2 < 100 or 1000 <= v2 < 10000 or v2 >= 100000:
                v1 += 1
        return v1
