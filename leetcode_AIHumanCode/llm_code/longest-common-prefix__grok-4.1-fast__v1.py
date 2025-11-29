class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        first, last = strs[0], strs[-1]
        idx = 0
        minlen = min(len(first), len(last))
        while idx < minlen and first[idx] == last[idx]:
            idx += 1
        return first[:idx]
