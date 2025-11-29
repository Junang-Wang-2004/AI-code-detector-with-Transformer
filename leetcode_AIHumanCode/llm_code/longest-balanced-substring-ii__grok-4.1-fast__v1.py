class Solution:
    def longestBalanced(self, s):
        ans = 0
        n = len(s)
        if n == 0:
            return 0
        # monochromatic
        curr_len = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                curr_len += 1
            else:
                ans = max(ans, curr_len)
                curr_len = 1
        ans = max(ans, curr_len)
        # bichromatic balanced
        pairs = [('a', 'b'), ('b', 'c'), ('c', 'a')]
        for p1, p2 in pairs:
            seen = {0: -1}
            delta = 0
            for i in range(n):
                ch = s[i]
                if ch == p1:
                    delta += 1
                elif ch == p2:
                    delta -= 1
                else:
                    seen = {0: i}
                    delta = 0
                    continue
                if delta in seen:
                    ans = max(ans, i - seen[delta])
                else:
                    seen[delta] = i
        # trichromatic balanced
        seen_tri = {(0, 0): -1}
        ca = cb = 0
        for i in range(n):
            if s[i] == 'a':
                ca += 1
            elif s[i] == 'b':
                cb += 1
            else:
                ca -= 1
                cb -= 1
            key = (ca, cb)
            if key in seen_tri:
                ans = max(ans, i - seen_tri[key])
            else:
                seen_tri[key] = i
        return ans
