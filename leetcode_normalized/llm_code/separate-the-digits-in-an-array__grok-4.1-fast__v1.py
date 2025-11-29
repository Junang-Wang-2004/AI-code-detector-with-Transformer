class C1:

    def separateDigits(self, a1):
        v1 = []
        for v2 in a1:
            v3 = []
            v4 = v2
            while v4:
                v3.append(v4 % 10)
                v4 //= 10
            v1.extend(v3[::-1])
        return v1
