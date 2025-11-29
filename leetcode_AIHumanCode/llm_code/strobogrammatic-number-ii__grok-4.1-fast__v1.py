class Solution:
    def findStrobogrammatic(self, n):
        valid_pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        outer_pairs = [('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        mids = ['0', '1', '8'] if n % 2 else ['']
        ans = mids
        for _ in range(n // 2):
            curlen = len(ans[0])
            prs = outer_pairs if curlen == n - 2 else valid_pairs
            newer = []
            for s in ans:
                for l, r in prs:
                    newer.append(l + s + r)
            ans = newer
        return ans
