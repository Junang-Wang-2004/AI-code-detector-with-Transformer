class C1:

    def average(self, a1):
        v1 = sorted(a1)
        return sum(v1[1:-1]) / (len(a1) - 2)
