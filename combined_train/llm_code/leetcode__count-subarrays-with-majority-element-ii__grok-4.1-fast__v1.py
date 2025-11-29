class C1:

    def countMajoritySubarrays(self, a1, a2):

        class FenwickTree:

            def __init__(self, a1):
                self.sz = a1
                self.tree = [0] * (a1 + 1)

            def update(self, a1, a2):
                a1 += 1
                while a1 <= self.sz:
                    self.tree[a1] += a2
                    a1 += a1 & -a1

            def query(self, a1):
                a1 += 1
                v2 = 0
                while a1 > 0:
                    v2 += self.tree[a1]
                    a1 -= a1 & -a1
                return v2
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = FenwickTree(2 * v1 + 1)
        v3 = v1
        v4 = 0
        v2.update(v3, 1)
        v5 = 0
        for v6 in a1:
            v4 += 1 if v6 == a2 else -1
            v5 += v2.query(v4 - 1 + v3)
            v2.update(v4 + v3, 1)
        return v5
