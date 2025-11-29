class Solution(object):
    def longestSubarray(self, nums, k):
        freq = {}
        dups = 0
        begin = 0
        maxlen = 0
        for i in range(len(nums)):
            x = nums[i]
            freq[x] = freq.get(x, 0) + 1
            if freq[x] == 2:
                dups += 1
            while dups > k:
                y = nums[begin]
                if freq[y] == 2:
                    dups -= 1
                freq[y] -= 1
                if freq[y] == 0:
                    del freq[y]
                begin += 1
            maxlen = max(maxlen, i - begin + 1)
        return maxlen
