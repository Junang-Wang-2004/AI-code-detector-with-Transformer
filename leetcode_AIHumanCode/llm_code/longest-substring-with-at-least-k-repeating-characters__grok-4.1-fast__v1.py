class Solution:
    def longestSubstring(self, s, k):
        ans = 0
        stk = [(0, len(s))]
        while stk:
            l, r = stk.pop()
            if r - l <= ans:
                continue
            freq = [0] * 26
            for i in range(l, r):
                freq[ord(s[i]) - ord('a')] += 1
            i = l
            while i < r:
                while i < r and freq[ord(s[i]) - ord('a')] < k:
                    i += 1
                if i == r:
                    break
                j = i
                while j < r and freq[ord(s[j]) - ord('a')] >= k:
                    j += 1
                sublen = j - i
                if i == l and j == r:
                    ans = max(ans, sublen)
                else:
                    stk.append((i, j))
                i = j
        return ans
