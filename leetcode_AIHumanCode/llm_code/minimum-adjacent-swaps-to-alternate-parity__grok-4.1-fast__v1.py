class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        ones_pos = [i for i in range(n) if nums[i] % 2]
        num_ones = len(ones_pos)
        even_targs = list(range(0, n, 2))
        odd_targs = list(range(1, n, 2))
        costs = []
        if num_ones == len(even_targs):
            costs.append(sum(abs(ones_pos[k] - even_targs[k]) for k in range(num_ones)))
        if num_ones == len(odd_targs):
            costs.append(sum(abs(ones_pos[k] - odd_targs[k]) for k in range(num_ones)))
        return min(costs) if costs else -1
