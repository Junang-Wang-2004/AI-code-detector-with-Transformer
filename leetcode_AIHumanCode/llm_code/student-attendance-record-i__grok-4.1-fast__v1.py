class Solution:
    def checkRecord(self, s):
        num_absences = 0
        streak_lates = 0
        for mark in s:
            if mark == 'A':
                num_absences += 1
                if num_absences > 1:
                    return False
                streak_lates = 0
            elif mark == 'L':
                streak_lates += 1
                if streak_lates >= 3:
                    return False
            else:
                streak_lates = 0
        return True
