import collections

class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        ways = [0] * (n + 1)
        ways[0] = 1
        prefix = [0] * (n + 2)
        prefix[1] = 1
        left = 0
        maxq = collections.deque()
        minq = collections.deque()
        for right in range(n):
            while maxq and nums[maxq[-1]] <= nums[right]:
                maxq.pop()
            maxq.append(right)
            while minq and nums[minq[-1]] >= nums[right]:
                minq.pop()
            minq.append(right)
            while left <= right and nums[maxq[0]] - nums[minq[0]] > k:
                if maxq and maxq[0] == left:
                    maxq.popleft()
                if minq and minq[0] == left:
                    minq.popleft()
                left += 1
            ways[right + 1] = (prefix[right + 1] - prefix[left] + MOD) % MOD
            prefix[right + 2] = (prefix[right + 1] + ways[right + 1]) % MOD
        return ways[n]
