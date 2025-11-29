import collections

class Solution:
    def minMaxSubarraySum(self, nums, k):
        def compute_sum(ascending):
            dq = collections.deque()
            prefix = 0
            outcome = 0
            length = len(nums)
            for pos in range(length):
                window_start = max(pos - k + 1, 0)
                while dq and not ((nums[dq[-1]] < nums[pos]) if ascending else (nums[dq[-1]] > nums[pos])):
                    idx = dq.pop()
                    prior = dq[-1] + 1 if dq else window_start
                    span = idx - prior + 1
                    prefix -= span * nums[idx]
                prior = dq[-1] + 1 if dq else window_start
                span = pos - prior + 1
                dq.append(pos)
                prefix += span * nums[pos]
                outcome += prefix
                if pos >= k - 1:
                    leave_pos = pos - k + 1
                    prefix -= nums[dq[0]]
                    if dq[0] == leave_pos:
                        dq.popleft()
            return outcome
        return compute_sum(True) + compute_sum(False)
