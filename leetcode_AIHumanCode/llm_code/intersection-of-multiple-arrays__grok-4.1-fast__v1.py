class Solution:
    def intersection(self, nums):
        if not nums:
            return []
        MAX_VAL = 1000
        appearances = [0] * (MAX_VAL + 1)
        for lst in nums:
            uniques = set(lst)
            for val in uniques:
                appearances[val] += 1
        common = []
        n_lists = len(nums)
        for idx in range(1, MAX_VAL + 1):
            if appearances[idx] == n_lists:
                common.append(idx)
        return common
