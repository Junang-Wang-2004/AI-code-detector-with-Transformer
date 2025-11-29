class Solution:
    def maxProduct(self, words):
        char_mask = {}
        for w in words:
            m = 0
            for c in set(w):
                m |= 1 << (ord(c) - 97)
            char_mask[m] = max(char_mask.get(m, 0), len(w))
        items = sorted([(ln, mk) for mk, ln in char_mask.items()], reverse=True)
        res = 0
        sz = len(items)
        for x in range(sz):
            a_len, a_mask = items[x]
            if a_len * a_len <= res:
                break
            for y in range(x + 1, sz):
                b_len, b_mask = items[y]
                if a_len * b_len <= res:
                    break
                if a_mask & b_mask == 0:
                    res = max(res, a_len * b_len)
        return res
