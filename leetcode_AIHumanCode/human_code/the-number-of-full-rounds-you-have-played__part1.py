# Time:  O(1)
# Space: O(1)

class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        """
        h1, m1 = list(map(int, startTime.split(":")))
        h2, m2 = list(map(int, finishTime.split(":")))
        start = h1*60+m1
        finish = h2*60+m2
        if start > finish:
            finish += 1440
        return max(finish//15-(start+15-1)//15, 0)


