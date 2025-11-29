class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        x, y = pattern
        pairs = 0
        suf_y = 0
        tot_x = 0
        tot_y = 0
        n = len(text)
        i = n - 1
        while i >= 0:
            c = text[i]
            if c == x:
                pairs += suf_y
                tot_x += 1
            if c == y:
                suf_y += 1
                tot_y += 1
            i -= 1
        return pairs + max(tot_x, tot_y)
