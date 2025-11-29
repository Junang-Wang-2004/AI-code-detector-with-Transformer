class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
        sum_to_last = {}
        endlen = [float('inf')] * n
        for i in range(n):
            curs = pref[i + 1]
            if curs - target in sum_to_last:
                j = sum_to_last[curs - target]
                endlen[i] = i - j
            sum_to_last[curs] = i
        minbefore = [float('inf')] * (n + 1)
        for k in range(1, n + 1):
            minbefore[k] = min(minbefore[k - 1], endlen[k - 1])
        res = float('inf')
        for i in range(n):
            if endlen[i] < float('inf'):
                startpos = i - endlen[i] + 1
                if startpos > 0:
                    res = min(res, minbefore[startpos] + endlen[i])
        return res if res < float('inf') else -1
