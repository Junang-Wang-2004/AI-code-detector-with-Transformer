class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def distinctSubarraysWithAtMostKOddIntegers(self, nums, limit):
        root = TrieNode()
        ans = 0
        start = 0
        odd_cnt = 0
        n = len(nums)
        for end in range(n):
            odd_cnt += nums[end] % 2
            while odd_cnt > limit:
                odd_cnt -= nums[start] % 2
                start += 1
            curr = root
            new = 0
            for pos in range(end, start - 1, -1):
                val = nums[pos]
                if val not in curr.children:
                    new += 1
                    curr.children[val] = TrieNode()
                curr = curr.children[val]
            ans += new
        return ans
