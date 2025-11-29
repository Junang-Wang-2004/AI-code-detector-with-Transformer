# Time:  O(n)
# Space: O(1)
# greedy
class Solution2(object):
    def canMakeEqual(self, nums, k):
        """
        """
        def check(target):
            parity = cnt = 0
            for i in range(len(nums)):
                if nums[i] == target:
                    continue
                cnt += i if parity else -i
                if cnt > k:
                    return False
                parity ^= 1
            return parity == 0

        return check(1) or check(-1)
