class Solution:
    def maximumCoins(self, coins, k):
        def get_max(cns):
            cns = sorted(cns)
            n = len(cns)
            prefix = [0] * (n + 1)
            for idx in range(n):
                leng = cns[idx][1] - cns[idx][0] + 1
                prefix[idx + 1] = prefix[idx] + leng * cns[idx][2]
            max_val = 0
            lft = 0
            for rgt in range(n):
                while cns[rgt][1] - cns[lft][1] + 1 > k:
                    lft += 1
                tot = prefix[rgt + 1] - prefix[lft]
                spn = cns[rgt][1] - cns[lft][0] + 1
                pen = max(spn - k, 0) * cns[lft][2]
                max_val = max(max_val, tot - pen)
            return max_val
        
        ans = get_max(coins)
        flipped = [[-x[1], -x[0], x[2]] for x in coins]
        ans = max(ans, get_max(flipped))
        return ans
