# Time:  O(n)
# Space: O(k)

import collections


# two pointers, sliding window, mono deque
class Solution(object):
    def minMaxSubarraySum(self, nums, k):
        """
        """
        def count(check):
            result = total = 0
            dq = collections.deque()
            for right in range(len(nums)):
                while dq and not check(nums[dq[-1]], nums[right]):
                    i = dq.pop()
                    cnt = i-(dq[-1]+1 if dq else max(right-k+1, 0))+1
                    total -= cnt*nums[i]
                cnt = right-(dq[-1]+1 if dq else max(right-k+1, 0))+1
                dq.append(right)
                total += cnt*nums[right]
                result += total
                if right-(k-1) >= 0:
                    total -= nums[dq[0]]
                    if dq[0] == right-(k-1):
                        dq.popleft()
            return result
    
        return count(lambda a, b: a < b)+count(lambda a, b: a > b)


