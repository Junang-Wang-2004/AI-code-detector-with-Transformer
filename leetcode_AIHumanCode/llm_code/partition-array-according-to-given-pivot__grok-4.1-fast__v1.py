class Solution(object):
    def pivotArray(self, nums, pivot):
        smaller = []
        larger = []
        for val in nums:
            if val < pivot:
                smaller.append(val)
            elif val > pivot:
                larger.append(val)
        eq_cnt = len(nums) - len(smaller) - len(larger)
        return smaller + [pivot] * eq_cnt + larger
