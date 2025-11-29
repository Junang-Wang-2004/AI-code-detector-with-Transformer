# Time:  O(n)
# Space: O(n)
import collections


# mono deque, two pointers
class Solution2(object):
    def continuousSubarrays(self, nums):
        """
        """
        mn, mx = collections.deque(), collections.deque()
        result = left = 0
        for right in range(len(nums)):
            while mn and nums[mn[-1]] > nums[right]:
                mn.pop()
            mn.append(right)
            while mx and nums[mx[-1]] < nums[right]:
                mx.pop()
            mx.append(right)
            while not nums[right]-nums[mn[0]] <= 2:
                left = max(left, mn.popleft()+1)
            while not nums[mx[0]]-nums[right] <= 2:
                left = max(left, mx.popleft()+1)
            result += right-left+1
        return result


