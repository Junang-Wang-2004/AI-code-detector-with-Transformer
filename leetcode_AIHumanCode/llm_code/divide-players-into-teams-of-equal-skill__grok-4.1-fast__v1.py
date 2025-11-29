class Solution:
    def dividePlayers(self, skill):
        n = len(skill)
        if n == 0:
            return 0
        total = sum(skill)
        teams = n // 2
        if total % teams != 0:
            return -1
        pair_sum = total // teams
        skills = sorted(skill)
        left = 0
        right = n - 1
        chemistry = 0
        while left < right:
            if skills[left] + skills[right] != pair_sum:
                return -1
            chemistry += skills[left] * skills[right]
            left += 1
            right -= 1
        return chemistry
