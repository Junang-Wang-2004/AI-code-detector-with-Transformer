# Time:  O(n * logk)
# Space: O(k)
# Generalization of k-uplet.
class Solution_Generalization(object):
    def increasingTriplet(self, nums):
        """
        """
        def increasingKUplet(nums, k):
            inc = [float('inf')] * (k - 1)
            for num in nums:
                i = bisect.bisect_left(inc, num)
                if i >= k - 1:
                    return True
                inc[i] = num
            return k == 0

        return increasingKUplet(nums, 3)

