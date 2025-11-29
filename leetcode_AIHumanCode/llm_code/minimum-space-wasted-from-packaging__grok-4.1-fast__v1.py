class Solution:
    def minWastedSpace(self, packages, boxes):
        pkgs = sorted(packages)
        n = len(pkgs)
        if n == 0:
            return 0
        MOD = 10**9 + 7
        minwaste = float('inf')
        maxpkg = pkgs[-1]
        for boxset in boxes:
            bxs = sorted(boxset)
            if not bxs or bxs[-1] < maxpkg:
                continue
            pos = 0
            thiswaste = 0
            for cap in bxs:
                while pos < n and pkgs[pos] <= cap:
                    thiswaste += cap - pkgs[pos]
                    pos += 1
                if pos == n:
                    break
            if pos == n:
                minwaste = min(minwaste, thiswaste)
        return minwaste % MOD if minwaste != float('inf') else -1
