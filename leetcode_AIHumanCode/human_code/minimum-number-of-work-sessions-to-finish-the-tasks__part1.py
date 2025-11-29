# Time:  O(n * 2^n)
# Space: O(2^n)

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        """
        # dp[mask]: min used time by choosing tasks in mask bitset
        dp = [float("inf") for _ in range(1<<len(tasks))]
        dp[0] = 0
        for mask in range(len(dp)-1):
            basis = 1
            for task in tasks:
                new_mask = mask|basis
                basis <<= 1
                if new_mask == mask:
                    continue
                if dp[mask]%sessionTime + task > sessionTime:
                    task += sessionTime-dp[mask]%sessionTime  # take a break
                dp[new_mask] = min(dp[new_mask], dp[mask]+task)
        return (dp[-1]+sessionTime-1)//sessionTime


