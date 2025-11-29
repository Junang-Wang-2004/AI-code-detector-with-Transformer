class Solution(object):
    def maxFont(self, text, w, h, fonts, fontInfo):
        char_freq = {}
        for c in text:
            char_freq[c] = char_freq.get(c, 0) + 1

        def fits(idx):
            f = fonts[idx]
            if fontInfo.getHeight(f) > h:
                return False
            tot_w = 0
            for ch, num in char_freq.items():
                tot_w += num * fontInfo.getWidth(f, ch)
            return tot_w <= w

        l, r = 0, len(fonts) - 1
        while l <= r:
            m = l + (r - l) // 2
            if fits(m):
                l = m + 1
            else:
                r = m - 1
        return fonts[r] if r >= 0 else -1
