class C1:

    def beautifulIndices(self, a1: str, a2: str, a3: str, a4: int) -> list[int]:

        def extract_starts(a1: str) -> list[int]:
            v1 = []
            v2 = 0
            while True:
                v2 = a1.find(a1, v2)
                if v2 < 0:
                    break
                v1.append(v2)
                v2 += 1
            return v1
        v1 = extract_starts(a2)
        v2 = extract_starts(a3)
        v3 = []
        v4 = 0
        for v5 in v1:
            while v4 < len(v2) and v2[v4] < v5 - a4:
                v4 += 1
            if v4 < len(v2) and v2[v4] <= v5 + a4:
                v3.append(v5)
        return v3
