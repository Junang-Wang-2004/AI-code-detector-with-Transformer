class C1:

    def smallestNumber(self, a1, a2):
        v1 = a1
        while True:
            v2 = 1
            v3 = False
            for v4 in str(v1):
                v2 = v2 * int(v4) % a2
                if v2 == 0:
                    v3 = True
                    break
            if v3:
                return v1
            v1 += 1
