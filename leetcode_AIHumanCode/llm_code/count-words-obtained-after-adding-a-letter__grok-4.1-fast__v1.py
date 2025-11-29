class Solution:
    def wordCount(self, startWords, targetWords):
        def get_mask(s):
            res = 0
            for ch in s:
                res |= 1 << (ord(ch) - ord('a'))
            return res

        prefixes = {get_mask(p) for p in startWords}
        cnt = 0
        for t in targetWords:
            tmask = get_mask(t)
            if any((tmask ^ (1 << i)) in prefixes
                   for i in range(26) if tmask & (1 << i)):
                cnt += 1
        return cnt
