class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(scores)
        plist = sorted(zip(ages, scores))
        uniq_scores = sorted(set(scores))
        sz = len(uniq_scores)
        rank = {uniq_scores[j]: j + 1 for j in range(sz)}
        ftree = [0] * (sz + 2)
        
        def up(p, v):
            while p <= sz:
                ftree[p] = max(ftree[p], v)
                p += p & -p
        
        def q(p):
            res = 0
            while p > 0:
                res = max(res, ftree[p])
                p -= p & -p
            return res
        
        idx = 0
        while idx < n:
            this_age = plist[idx][0]
            grps = []
            while idx < n and plist[idx][0] == this_age:
                grps.append(plist[idx][1])
                idx += 1
            updates = []
            for s in grps:
                rp = rank[s]
                prevmax = q(rp)
                updates.append((rp, prevmax + s))
            for rp, val in updates:
                up(rp, val)
        return q(sz)
