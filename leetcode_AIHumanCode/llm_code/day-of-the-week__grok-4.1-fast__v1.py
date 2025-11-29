class Solution:
    def dayOfTheWeek(self, day, month, year):
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        moff = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        ay = year - (month < 3)
        res = (ay + ay // 4 - ay // 100 + ay // 400 + moff[month - 1] + day) % 7
        return weekdays[res]
