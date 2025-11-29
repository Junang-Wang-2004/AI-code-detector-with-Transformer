class Solution(object):
    def longestCommomSubsequence(self, arrays):
        if not arrays:
            return []
        idx = min(range(len(arrays)), key=lambda k: len(arrays[k]))
        base = arrays[idx]
        if not base:
            return []
        matches = set(base)
        for seq in arrays:
            matches &= set(seq)
            if not matches:
                return []
        return [elem for elem in base if elem in matches]
