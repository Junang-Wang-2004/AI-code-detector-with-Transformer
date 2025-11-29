class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        min_len = float('inf')
        ans = ""
        for i in range(n):
            if s[i] != '1':
                continue
            ones = 1
            j = i
            while j < n and ones < k:
                j += 1
                if s[j] == '1':
                    ones += 1
            if ones == k:
                sub = s[i:j + 1]
                length = len(sub)
                if length < min_len:
                    min_len = length
                    ans = sub
                elif length == min_len and sub < ans:
                    ans = sub
        return ans
