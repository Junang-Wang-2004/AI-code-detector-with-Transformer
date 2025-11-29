import bisect

class Solution:
    def maxDepthBST(self, order):
        depths = {}
        sorted_keys = []
        max_depth = 0
        for val in order:
            pos = bisect.bisect_left(sorted_keys, val)
            left_depth = depths[sorted_keys[pos - 1]] if pos > 0 else 0
            right_depth = depths[sorted_keys[pos]] if pos < len(sorted_keys) else 0
            curr_depth = 1 + max(left_depth, right_depth)
            depths[val] = curr_depth
            max_depth = max(max_depth, curr_depth)
            bisect.insort_left(sorted_keys, val)
        return max_depth
