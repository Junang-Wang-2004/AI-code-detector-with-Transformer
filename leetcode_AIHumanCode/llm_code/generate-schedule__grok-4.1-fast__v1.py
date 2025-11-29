class Solution(object):
    def generateSchedule(self, n):
        if n <= 4:
            return []
        schedule = []
        for delta in range(1, n):
            for idx in range(n):
                schedule.append([idx, (idx + delta) % n])
        return schedule
