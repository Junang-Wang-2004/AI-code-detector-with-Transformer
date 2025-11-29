class NumArray:
    def __init__(self, values):
        length = len(values)
        self.prefix_sums = [0] * (length + 1)
        for pos in range(1, length + 1):
            self.prefix_sums[pos] = self.prefix_sums[pos - 1] + values[pos - 1]

    def sumRange(self, start, end):
        return self.prefix_sums[end + 1] - self.prefix_sums[start]
