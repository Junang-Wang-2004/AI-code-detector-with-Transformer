# Time:  O(n^3 * a^2)
# Space: O(n^2)

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        """
        MAX_ANS = 1000
        n = (len(s)+1)//2
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].add(int(s[i*2]))
        for l in range(1, n):
            for left in range(n-l):
                right = left+l
                for k in range(left, right):
                    if s[2*k+1] == '+':
                        dp[left][right].update((x+y for x in dp[left][k] for y in dp[k+1][right] if x+y <= MAX_ANS))
                    else:
                        dp[left][right].update((x*y for x in dp[left][k] for y in dp[k+1][right] if x*y <= MAX_ANS))
        target = eval(s)
        return sum(5 if ans == target else 2 if ans in dp[0][-1] else 0 for ans in answers)


