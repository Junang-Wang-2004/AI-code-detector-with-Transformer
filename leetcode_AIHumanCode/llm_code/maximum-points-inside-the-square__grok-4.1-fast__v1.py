class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        INF = float('inf')
        first = [INF] * 26
        second = [INF] * 26
        n = len(points)
        for i in range(n):
            x, y = points[i]
            r = max(abs(x), abs(y))
            k = ord(s[i]) - ord('a')
            if r < first[k]:
                second[k] = first[k]
                first[k] = r
            elif r < second[k]:
                second[k] = r
        thresh = INF
        for j in range(26):
            if second[j] < INF:
                thresh = min(thresh, second[j])
        res = 0
        for j in range(26):
            if first[j] < thresh:
                res += 1
        return res
