class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        total = len(nums)
        count_small = (total + 1) // 2
        count_large = total // 2
        small_part = [nums[count_small - 1 - p] for p in range(count_small)]
        large_part = [nums[total - 1 - q] for q in range(count_large)]
        s_idx, l_idx = 0, 0
        for pos in range(total):
            if pos % 2 == 0:
                nums[pos] = small_part[s_idx]
                s_idx += 1
            else:
                nums[pos] = large_part[l_idx]
                l_idx += 1
        return nums
