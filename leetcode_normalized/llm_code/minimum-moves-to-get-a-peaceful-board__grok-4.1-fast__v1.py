class C1:

    def minMoves(self, a1):
        v1 = [pos[0] for v2 in a1]
        v3 = [v2[1] for v2 in a1]

        def total_cost(a1):
            v1 = sorted(a1)
            return sum((abs(v1[i] - i) for v2 in range(len(v1))))
        return total_cost(v1) + total_cost(v3)
