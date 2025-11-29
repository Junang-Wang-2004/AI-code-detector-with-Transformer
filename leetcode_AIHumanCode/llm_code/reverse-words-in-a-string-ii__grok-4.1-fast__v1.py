class Solution(object):
    def reverseWords(self, s):
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        pos = 0
        while pos < len(s):
            while pos < len(s) and s[pos] == ' ':
                pos += 1
            if pos >= len(s):
                break
            nxt = pos
            while nxt < len(s) and s[nxt] != ' ':
                nxt += 1
            lft, rgt = pos, nxt - 1
            while lft < rgt:
                s[lft], s[rgt] = s[rgt], s[lft]
                lft += 1
                rgt -= 1
            pos = nxt
