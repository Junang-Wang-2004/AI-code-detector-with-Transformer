class Solution:
    def expressiveWords(self, S, words):
        def parse_groups(st):
            groups = []
            i = 0
            n = len(st)
            while i < n:
                start = i
                while i < n and st[i] == st[start]:
                    i += 1
                groups.append((st[start], i - start))
            return groups

        s_groups = parse_groups(S)
        ans = 0
        for w in words:
            w_groups = parse_groups(w)
            if len(s_groups) != len(w_groups):
                continue
            valid = True
            for (sc, slen), (wc, wlen) in zip(s_groups, w_groups):
                if sc != wc or not (slen == wlen or slen >= 3 and slen >= wlen):
                    valid = False
                    break
            if valid:
                ans += 1
        return ans
