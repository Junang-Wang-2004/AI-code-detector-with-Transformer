class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window_set = set()
        for idx in range(len(nums)):
            if nums[idx] in window_set:
                return True
            window_set.add(nums[idx])
            if idx >= k:
                window_set.remove(nums[idx - k])
        return False
