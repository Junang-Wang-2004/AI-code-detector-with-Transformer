class Solution:
    def minOperations(self, grid, x):
        values = []
        for line in grid:
            values.extend(line)
        mods = {v % x for v in values}
        if len(mods) > 1:
            return -1
        values.sort()
        center = values[len(values) // 2]
        ops = 0
        for v in values:
            ops += abs(v - center) // x
        return ops
