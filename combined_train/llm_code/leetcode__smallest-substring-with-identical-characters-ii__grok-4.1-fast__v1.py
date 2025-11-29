class C1:

    def minLength(self, a1: str, a2: int) -> int:

        def compute_run_lengths(a1):
            if not a1:
                return []
            v1 = []
            v2 = 1
            for v3 in range(1, len(a1)):
                if a1[v3] == a1[v3 - 1]:
                    v2 += 1
                else:
                    v1.append(v2)
                    v2 = 1
            v1.append(v2)
            return v1
        v1 = compute_run_lengths(a1)
        v2 = len(a1)

        def feasible(a1):
            if a1 == 1:
                v1 = sum((1 for v2 in range(v2) if int(a1[v2]) != v2 % 2))
                return min(v1, v2 - v1) <= a2
            v3 = sum((ln // (a1 + 1) for v4 in v1))
            return v3 <= a2
        v3 = 1
        v4 = v2
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if feasible(v5):
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        return v3
