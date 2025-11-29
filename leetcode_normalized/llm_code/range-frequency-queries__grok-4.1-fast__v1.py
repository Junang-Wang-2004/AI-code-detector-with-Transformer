class C1:

    def __init__(self, a1):
        self.occurrences = {}
        for v1, v2 in enumerate(a1):
            self.occurrences.setdefault(v2, []).append(v1)

    def _find_first_ge(self, a1, a2):
        v1, v2 = (0, len(a1))
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if a1[v3] < a2:
                v1 = v3 + 1
            else:
                v2 = v3
        return v1

    def _find_first_gt(self, a1, a2):
        v1, v2 = (0, len(a1))
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if a1[v3] <= a2:
                v1 = v3 + 1
            else:
                v2 = v3
        return v1

    def query(self, a1, a2, a3):
        v1 = self.occurrences.get(a3, [])
        return self._find_first_gt(v1, a2) - self._find_first_ge(v1, a1)
