class C1:

    def fillCups(self, a1):
        v1 = sorted(a1, reverse=True)
        v2, v3, v4 = v1
        v5 = v2 + v3 + v4
        if v2 > v3 + v4:
            return v2
        return (v5 + 1) // 2
