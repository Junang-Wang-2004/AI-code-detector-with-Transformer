class Solution:
    def dayOfYear(self, date):
        y, mo, d = map(int, date.split('-'))
        mo_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ans = sum(mo_days[:mo - 1]) + d
        if mo > 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
            ans += 1
        return ans
