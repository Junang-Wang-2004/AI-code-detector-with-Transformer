class Solution:
    def matchReplacement(self, s, sub, mappings):
        can_replace = {}
        for x, y in mappings:
            if x not in can_replace:
                can_replace[x] = set()
            can_replace[x].add(y)
        
        slen, plen = len(s), len(sub)
        for start in range(slen - plen + 1):
            mismatch = False
            for idx in range(plen):
                pat_char = sub[idx]
                str_char = s[start + idx]
                if pat_char != str_char and str_char not in can_replace.get(pat_char, set()):
                    mismatch = True
                    break
            if not mismatch:
                return True
        return False
