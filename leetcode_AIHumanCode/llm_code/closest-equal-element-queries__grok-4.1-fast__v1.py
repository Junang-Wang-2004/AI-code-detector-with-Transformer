class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        pos_map = {}
        for i in range(n):
            v = nums[i]
            if v not in pos_map:
                pos_map[v] = []
            pos_map[v].append(i)
        mins = [n] * n
        for v, positions in pos_map.items():
            sz = len(positions)
            if sz < 2:
                continue
            for j in range(sz):
                p_prev = positions[(j - 1) % sz]
                p_next = positions[(j + 1) % sz]
                d1 = (positions[j] - p_prev + n) % n
                d2 = (p_next - positions[j] + n) % n
                mins[positions[j]] = min(mins[positions[j]], min(d1, d2))
        res = []
        for q in queries:
            res.append(mins[q] if mins[q] < n else -1)
        return res
