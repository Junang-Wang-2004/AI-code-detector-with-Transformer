class C1:

    def numOfBurgers(self, a1, a2):
        if a1 % 2:
            return []
        v1 = a1 // 2
        if v1 < a2 or v1 > a2 * 2:
            return []
        v2 = v1 - a2
        v3 = a2 * 2 - v1
        return [v2, v3]
