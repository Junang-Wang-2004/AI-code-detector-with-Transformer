class C1:

    def countEven(self, a1):
        v1 = str(a1)
        v2 = sum((int(c) for v3 in v1)) % 2
        return (a1 - v2) // 2
