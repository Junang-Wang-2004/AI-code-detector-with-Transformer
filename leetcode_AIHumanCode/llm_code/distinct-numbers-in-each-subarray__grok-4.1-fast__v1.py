class Solution(object):
    def distinctNumbers(self, nums, k):
        freq_map = {}
        result_list = []
        n = len(nums)
        for r in range(n):
            curr = nums[r]
            if curr in freq_map:
                freq_map[curr] += 1
            else:
                freq_map[curr] = 1
            if r >= k - 1:
                result_list.append(len(freq_map))
                left_val = nums[r - k + 1]
                freq_map[left_val] -= 1
                if freq_map[left_val] == 0:
                    del freq_map[left_val]
        return result_list
