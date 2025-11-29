import collections

class Solution:
    def shortestSubarray(self, nums, K):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        ans = float('inf')
        dq = collections.deque()
        for i in range(len(prefix)):
            while dq and prefix[dq[-1]] >= prefix[i]:
                dq.pop()
            while dq and prefix[i] - prefix[dq[0]] >= K:
                ans = min(ans, i - dq.popleft())
            dq.append(i)
        return ans if ans < float('inf') else -1
