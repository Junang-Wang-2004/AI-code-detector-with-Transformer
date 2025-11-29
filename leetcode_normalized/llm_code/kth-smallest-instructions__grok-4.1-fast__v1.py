class C1:

    def kthSmallestPath(self, a1, a2):
        v1, v2 = a1

        def binomial(a1, a2):
            if a2 == 0 or a2 == a1:
                return 1
            a2 = min(a2, a1 - a2)
            v2 = 1
            for v3 in range(a2):
                v2 = v2 * (a1 - v3) // (v3 + 1)
            return v2

        def construct_path(a1, a2, a3):
            if a1 == 0 and a2 == 0:
                return ''
            v1 = 0 if a2 == 0 else binomial(a1 + a2 - 1, a1)
            if a3 <= v1:
                return 'H' + construct_path(a1, a2 - 1, a3)
            else:
                return 'V' + construct_path(a1 - 1, a2, a3 - v1)
        return construct_path(v1, v2, a2)
