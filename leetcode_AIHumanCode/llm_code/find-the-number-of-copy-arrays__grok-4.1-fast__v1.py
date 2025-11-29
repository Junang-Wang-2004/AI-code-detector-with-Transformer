class Solution(object):
    def countArrays(self, original, bounds):
        n = len(original)
        min_val, max_val = bounds[0]
        shift = 0
        for j in range(1, n):
            delta = original[j] - original[j - 1]
            shift += delta
            min_val = max(min_val, bounds[j][0] - shift)
            max_val = min(max_val, bounds[j][1] - shift)
        return max(0, max_val - min_val + 1)
