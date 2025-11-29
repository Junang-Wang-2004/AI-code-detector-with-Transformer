# Time:  O(nlogn)
# Space: O(n)
import collections


# binary search, mono deque
class Solution2(object):
    def minCost(self, nums, x):
        """
        """
        def cost(k):
            w = k+1
            result = x*k
            dq = collections.deque()
            for i in range(len(nums)+w-1):
                if dq and i-dq[0] == w:
                    dq.popleft()
                while dq and nums[dq[-1]%len(nums)] >= nums[i%len(nums)]:
                    dq.pop()
                dq.append(i)
                if i >= w-1:
                    result += nums[dq[0]%len(nums)]
            return result

        def check(x):
            return cost(x) <= cost(x+1)

        left, right = 0, len(nums)
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return cost(left)


