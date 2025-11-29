# Time:  O(t)
# Space: O(t)
class Solution2(object):
    def largestNumber(self, cost, target):
        """
        """
        def key(bag):
            return sum(bag), bag
        
        dp = [[0]*9]
        for t in range(1, target+1):
            dp.append([])
            for d, c in enumerate(cost):
                if t < c or not dp[t-c]:
                    continue
                curr = dp[t-c][:]
                curr[~d] += 1
                if key(curr) > key(dp[t]):
                    dp[-1] = curr        
        if not dp[-1]:
            return "0"
        return "".join(str(9-i)*c for i, c in enumerate(dp[-1]))


