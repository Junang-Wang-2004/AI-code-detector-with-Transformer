class C1(object):

    def minOperations(self, a1, a2):
        v1 = sum((abs(a - b) for v2, v3 in zip(a1, a2)))
        v4 = a2[-1]
        v5 = min((0 if min(v2, v3) <= v4 <= max(v2, v3) else min(abs(v4 - v2), abs(v4 - v3)) for v2, v3 in zip(a1, a2)))
        return v1 + 1 + v5
