# Time:  O(1)
# Space: O(1)
import datetime


class Solution2(object):
    def daysBetweenDates(self, date1, date2):        
        delta = datetime.datetime.strptime(date1, "%Y-%m-%d")
        delta -= datetime.datetime.strptime(date2, "%Y-%m-%d")
        return abs(delta.days)
