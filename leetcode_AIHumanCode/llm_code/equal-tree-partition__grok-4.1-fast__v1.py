class Solution(object):
    def checkEqualTree(self, root):
        sub_sums = set()
        zero_cnt = [0]
        def dfs(nd):
            if not nd:
                return 0
            lsum = dfs(nd.left)
            rsum = dfs(nd.right)
            cursum = nd.val + lsum + rsum
            if cursum != 0:
                sub_sums.add(cursum)
            else:
                zero_cnt[0] += 1
            return cursum
        total = dfs(root)
        if total == 0:
            return zero_cnt[0] > 1
        return total % 2 == 0 and total // 2 in sub_sums
