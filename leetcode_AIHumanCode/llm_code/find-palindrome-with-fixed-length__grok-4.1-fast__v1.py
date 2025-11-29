class Solution:
    def kthPalindrome(self, queries, intLength):
        ans = []
        h = (intLength - 1) // 2
        low = 10 ** h
        high = 10 ** (h + 1) - 1
        div = intLength // 2
        for idx in queries:
            val = low + idx - 1
            if val > high:
                ans.append(-1)
                continue
            txt = str(val)
            left = txt[:div]
            center = txt[div] if intLength % 2 else ''
            right = left[::-1]
            ans.append(int(left + center + right))
        return ans
