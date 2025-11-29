class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        n = len(sweetness)
        total_sum = sum(sweetness)
        low = min(sweetness)
        high = total_sum // (K + 1)
        def feasible(target):
            idx = 0
            parts = 0
            while idx < n:
                acc = 0
                while idx < n and acc < target:
                    acc += sweetness[idx]
                    idx += 1
                if acc >= target:
                    parts += 1
            return parts >= K + 1
        while low <= high:
            m = low + (high - low) // 2
            if feasible(m):
                low = m + 1
            else:
                high = m - 1
        return high
