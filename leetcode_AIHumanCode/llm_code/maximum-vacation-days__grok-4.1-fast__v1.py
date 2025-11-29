class Solution(object):
    def maxVacationDays(self, flights, days):
        if not days or not flights:
            return 0
        n = len(days)
        k = len(days[0])
        prev = [-1] * n
        prev[0] = 0
        for w in range(k):
            curr = [-1] * n
            for i in range(n):
                if prev[i] == -1:
                    continue
                curr[i] = max(curr[i], prev[i] + days[i][w])
                for j in range(n):
                    if flights[i][j]:
                        curr[j] = max(curr[j], prev[i] + days[j][w])
            prev = curr
        return max(prev)
