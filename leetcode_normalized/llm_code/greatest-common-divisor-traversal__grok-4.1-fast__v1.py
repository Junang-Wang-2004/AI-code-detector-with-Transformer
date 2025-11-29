class C1:

    def canTraverseAllPairs(self, a1):
        v1 = len(a1)
        if v1 <= 1:
            return True
        v2 = max(a1)
        v3 = self._generate_primes(int(v2 ** 0.5) + 1)

        def extract_primes(a1):
            v1 = set()
            v2 = a1
            for v3 in v3:
                if v3 * v3 > v2:
                    break
                if v2 % v3 == 0:
                    v1.add(v3)
                    while v2 % v3 == 0:
                        v2 //= v3
            if v2 > 1:
                v1.add(v2)
            return v1

        def find_root(a1, a2):
            if a2[a1] != a1:
                a2[a1] = find_root(a2[a1], a2)
            return a2[a1]

        def merge_sets(a1, a2, a3, a4):
            v1 = find_root(a1, a3)
            v2 = find_root(a2, a3)
            if v1 == v2:
                return
            if a4[v1] < a4[v2]:
                a3[v1] = v2
            elif a4[v1] > a4[v2]:
                a3[v2] = v1
            else:
                a3[v2] = v1
                a4[v1] += 1
        v4 = list(range(v1))
        v5 = [0] * v1
        v6 = {}
        for v7, v8 in enumerate(a1):
            if v8 <= 1:
                continue
            v9 = extract_primes(v8)
            for v10 in v9:
                if v10 in v6:
                    merge_sets(v7, v6[v10], v4, v5)
                v6[v10] = v7
        v11 = find_root(0, v4)
        for v12 in range(1, v1):
            if find_root(v12, v4) != v11:
                return False
        return True

    def _generate_primes(self, a1):
        if a1 < 2:
            return []
        v1 = [True] * (a1 + 1)
        v1[0] = v1[1] = False
        for v2 in range(2, int(a1 ** 0.5) + 1):
            if v1[v2]:
                for v3 in range(v2 * v2, a1 + 1, v2):
                    v1[v3] = False
        return [idx for v4 in range(2, a1 + 1) if v1[v4]]
