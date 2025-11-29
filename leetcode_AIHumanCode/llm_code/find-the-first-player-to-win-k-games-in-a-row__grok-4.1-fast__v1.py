class Solution(object):
    def findWinningPlayer(self, skills, k):
        champion = 0
        streak = 0
        idx = 1
        n = len(skills)
        while idx < n:
            if skills[champion] >= skills[idx]:
                streak += 1
            else:
                champion = idx
                streak = 1
            if streak == k:
                return champion
            idx += 1
        return champion
