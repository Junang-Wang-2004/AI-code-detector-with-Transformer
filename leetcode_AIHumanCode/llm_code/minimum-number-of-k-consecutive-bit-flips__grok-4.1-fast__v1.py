from collections import deque

class Solution(object):
    def minKBitFlips(self, nums, k):
        n = len(nums)
        window = deque()
        parity = 0
        ops = 0
        for i in range(n):
            if window and window[0] == i - k:
                window.popleft()
                parity ^= 1
            if nums[i] == parity:
                if i + k > n:
                    return -1
                window.append(i)
                parity ^= 1
                ops += 1
        return ops
