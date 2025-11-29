from collections import Counter

class Solution:
    def maxEqualFreq(self, nums):
        count = Counter()
        freq = Counter()
        ans = 0
        n = len(nums)
        for length in range(1, n + 1):
            val = nums[length - 1]
            prev_freq = count[val]
            if prev_freq > 0:
                freq[prev_freq] -= 1
            count[val] += 1
            curr_freq = count[val]
            freq[curr_freq] += 1
            is_valid = False
            if len(freq) == 1:
                is_valid = True
            elif len(freq) == 2:
                fs = sorted(freq)
                lo, hi = fs[0], fs[1]
                if freq[hi] == 1 and hi == lo + 1:
                    is_valid = True
                elif lo == 1 and freq[1] == 1:
                    is_valid = True
            if is_valid:
                ans = length
        return ans
