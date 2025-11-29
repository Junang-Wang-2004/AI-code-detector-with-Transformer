import collections


class Solution(object):
    def maxRepOpt1(self, text):
        cnt = collections.Counter(text)
        res = 0
        n = len(text)
        for c in cnt:
            nones = 0
            l = 0
            for r in range(n):
                if text[r] != c:
                    nones += 1
                while nones > 1 and l <= r:
                    if text[l] != c:
                        nones -= 1
                    l += 1
                length = r - l + 1
                res = max(res, min(length, cnt[c]))
        return res
