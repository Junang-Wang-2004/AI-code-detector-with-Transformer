class C1:

    def __init__(self, a1):
        v1 = len(a1)
        self.prefix_sums = [0] * (v1 + 1)
        for v2 in range(1, v1 + 1):
            self.prefix_sums[v2] = self.prefix_sums[v2 - 1] + a1[v2 - 1]

    def sumRange(self, a1, a2):
        return self.prefix_sums[a2 + 1] - self.prefix_sums[a1]
