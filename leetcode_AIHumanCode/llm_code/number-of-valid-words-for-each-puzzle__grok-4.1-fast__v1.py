import collections

class Solution:
    def findNumOfValidWords(self, words, puzzles):
        cnt = collections.Counter()
        for w in words:
            msk = 0
            for ch in w:
                msk |= (1 << (ord(ch) - ord('a')))
            cnt[msk] += 1
        
        res = []
        for p in puzzles:
            pmask = 0
            fidx = ord(p[0]) - ord('a')
            fmask = 1 << fidx
            for ch in p:
                pmask |= (1 << (ord(ch) - ord('a')))
            
            total = 0
            submask = pmask
            while submask:
                if submask & fmask:
                    total += cnt[submask]
                submask = (submask - 1) & pmask
            
            res.append(total)
        return res
