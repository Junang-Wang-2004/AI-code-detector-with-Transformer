class Solution:
    def minimumSeconds(self, nums):
        n = len(nums)
        positions_by_val = {}
        for i, val in enumerate(nums):
            if val not in positions_by_val:
                positions_by_val[val] = []
            positions_by_val[val].append(i)
        result = n
        for pos_list in positions_by_val.values():
            k = len(pos_list)
            if k == 0:
                continue
            largest_gap = pos_list[0] + n - pos_list[-1]
            for j in range(k - 1):
                largest_gap = max(largest_gap, pos_list[j + 1] - pos_list[j])
            result = min(result, largest_gap // 2)
        return result
