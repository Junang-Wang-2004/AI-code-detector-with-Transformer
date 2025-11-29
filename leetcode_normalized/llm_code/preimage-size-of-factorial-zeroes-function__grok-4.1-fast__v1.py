class C1:

    def preimageSizeFZF(self, a1):

        def zeros(a1):
            v1 = 0
            while a1:
                a1 //= 5
                v1 += a1
            return v1

        def first_ge(a1):
            v1, v2 = (0, 5 * (a1 + 1))
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if zeros(v3) >= a1:
                    v2 = v3
                else:
                    v1 = v3 + 1
            return v1
        v1 = first_ge(a1)
        v2 = first_ge(a1 + 1) - 1
        if zeros(v1) != a1:
            return 0
        return v2 - v1 + 1
