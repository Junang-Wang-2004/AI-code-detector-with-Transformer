class Solution(object):
    def findAnagrams(self, s, p):
        if not p or len(p) > len(s):
            return []
        ans = []
        freq_p = [0] * 26
        for char in p:
            freq_p[ord(char) - ord('a')] += 1
        freq_win = [0] * 26
        plen = len(p)
        for i in range(plen):
            freq_win[ord(s[i]) - ord('a')] += 1
        if freq_win == freq_p:
            ans.append(0)
        for i in range(plen, len(s)):
            freq_win[ord(s[i - plen]) - ord('a')] -= 1
            freq_win[ord(s[i]) - ord('a')] += 1
            if freq_win == freq_p:
                ans.append(i - plen + 1)
        return ans
