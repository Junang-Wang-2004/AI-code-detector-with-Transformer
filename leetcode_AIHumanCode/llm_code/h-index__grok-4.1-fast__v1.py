class Solution:
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        from bisect import bisect_left
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            cnt = n - bisect_left(citations, mid)
            if cnt >= mid:
                left = mid
            else:
                right = mid - 1
        return left
