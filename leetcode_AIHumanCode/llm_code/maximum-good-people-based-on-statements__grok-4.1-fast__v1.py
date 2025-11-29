class Solution:
    def maximumGood(self, statements):
        n = len(statements)
        ans = 0
        for mask in range(1 << n):
            ok = True
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    continue
                for j in range(n):
                    stmt = statements[i][j]
                    if stmt == 2:
                        continue
                    is_good_j = bool(mask & (1 << j))
                    if is_good_j != bool(stmt):
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                cnt = 0
                x = mask
                while x:
                    cnt += 1
                    x &= x - 1
                ans = max(ans, cnt)
        return ans
