class C1:

    def minimumCost(self, a1):

        def compute_median(a1):
            v1 = sorted(a1)
            v2 = len(v1)
            v3 = v2 // 2
            if v2 % 2:
                return v1[v3]
            return (v1[v3 - 1] + v1[v3]) // 2

        def generate_palindromes(a1):
            v1 = str(a1)
            v2 = len(v1)
            v3 = set()
            v3.add(10 ** v2 + 1)
            v3.add(10 ** (v2 - 1) - 1)
            v4 = (v2 + 1) // 2
            v5 = int(v1[:v4])
            for v6 in (-1, 0, 1):
                v7 = v5 + v6
                if v7 <= 0:
                    continue
                v8 = str(v7)
                v9 = v8[:-1][::-1] if v2 % 2 else v8[::-1]
                v10 = int(v8 + v9)
                v3.add(v10)
            return v3
        v1 = compute_median(a1)
        v2 = generate_palindromes(v1)

        def calc_cost(a1):
            return sum((abs(x - a1) for v1 in a1))
        return min((calc_cost(p) for v3 in v2))
