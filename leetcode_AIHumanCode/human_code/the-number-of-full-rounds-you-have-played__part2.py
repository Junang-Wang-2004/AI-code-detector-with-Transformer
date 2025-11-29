# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        """
        h1, m1 = list(map(int, startTime.split(":")))
        h2, m2 = list(map(int, finishTime.split(":")))
        if m1 > m2:
            h2 -= 1
            m2 += 60
        return max((h2-h1)%24*4 + m2//15 - (m1+15-1)//15, 0)
