class C1:

    def combine(self, a1, a2):
        v1 = []

        def rec(a1, a2):
            if len(a1) == a2:
                v1.append(list(a1))
                return
            for v1 in range(a2, a1 + 1):
                a1.append(v1)
                rec(a1, v1 + 1)
                a1.pop()
        rec([], 1)
        return v1
