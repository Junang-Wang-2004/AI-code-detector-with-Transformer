class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)
        gaps = []
        if n > 0:
            gaps.append(startTime[0])
            for j in range(1, n):
                gaps.append(startTime[j] - endTime[j - 1])
            gaps.append(eventTime - endTime[-1])
        else:
            gaps.append(eventTime)
        mx = 0
        sm = 0
        for idx in range(len(gaps)):
            sm += gaps[idx]
            mx = max(mx, sm)
            if idx - k >= 0:
                sm -= gaps[idx - k]
        return mx
