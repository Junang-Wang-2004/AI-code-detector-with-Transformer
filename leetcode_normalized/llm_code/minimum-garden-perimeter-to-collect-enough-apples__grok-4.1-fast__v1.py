class C1:

    def minimumPerimeter(self, a1):
        v1 = 0
        v2 = 200000
        while v1 < v2:
            v3 = v1 + (v2 - v1) // 2
            if v3 * (2 * v3 + 1) * (2 * v3 + 2) >= a1:
                v2 = v3
            else:
                v1 = v3 + 1
        return 8 * v1
