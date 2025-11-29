from random import randint

class Solution:
    def findKthLargest(self, nums, k):
        def partition(lo, hi):
            pidx = randint(lo, hi)
            nums[pidx], nums[hi] = nums[hi], nums[pidx]
            pv = nums[hi]
            i = lo - 1
            for j in range(lo, hi):
                if nums[j] >= pv:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
            return i + 1

        begin, finish = 0, len(nums) - 1
        goal = k - 1
        while begin <= finish:
            pivot_pos = partition(begin, finish)
            if pivot_pos == goal:
                return nums[pivot_pos]
            elif pivot_pos > goal:
                finish = pivot_pos - 1
            else:
                begin = pivot_pos + 1
