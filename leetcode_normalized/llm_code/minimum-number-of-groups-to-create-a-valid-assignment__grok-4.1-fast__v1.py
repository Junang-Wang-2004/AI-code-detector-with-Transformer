import collections

class C1:

    def minGroupsForValidAssignment(self, a1):
        v1 = collections.Counter(a1)
        v2 = list(v1.values())
        if not v2:
            return 0
        v3 = min(v2)
        for v4 in range(v3, 0, -1):
            v5 = v4 + 1
            v6 = [(f + v5 - 1) // v5 for v7 in v2]
            if all((g * v4 <= v7 for v7, v8 in zip(v2, v6))):
                return sum(v6)
        return 0
