class C1:

    def getStrongest(self, a1, a2):
        v1 = sorted(a1)
        v2 = v1[(len(v1) - 1) // 2]

        def strength(a1):
            return (abs(a1 - v2), a1)
        return sorted(a1, key=strength, reverse=True)[:a2]
