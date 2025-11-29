class Solution:
    def plusOne(self, digits):
        val = 0
        for d in digits:
            val = val * 10 + d
        val += 1
        ans = []
        while val:
            ans.append(val % 10)
            val //= 10
        return ans[::-1]
