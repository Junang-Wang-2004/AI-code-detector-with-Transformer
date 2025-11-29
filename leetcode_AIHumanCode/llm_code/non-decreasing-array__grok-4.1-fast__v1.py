class Solution(object):
    def checkPossibility(self, nums):
        n = len(nums)
        for k in range(1, n):
            if nums[k - 1] > nums[k]:
                break
        else:
            return True

        # Try changing nums[k-1] to nums[k]
        suffix_ok1 = True
        can_change_left = (k < 2 or nums[k - 2] <= nums[k])
        if can_change_left:
            for i in range(k + 1, n):
                if nums[i - 1] > nums[i]:
                    suffix_ok1 = False
                    break
            if suffix_ok1:
                return True

        # Try changing nums[k] to nums[k-1]
        suffix_ok2 = True
        if k + 1 < n:
            if nums[k - 1] > nums[k + 1]:
                suffix_ok2 = False
            else:
                for i in range(k + 2, n):
                    if nums[i - 1] > nums[i]:
                        suffix_ok2 = False
                        break
        if suffix_ok2:
            return True

        return False
