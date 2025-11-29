class Solution(object):
    def containsPattern(self, arr, m, k):
        n = len(arr)
        idx = 0
        req = m * (k - 1)
        while idx < n - m:
            if arr[idx] != arr[idx + m]:
                idx += 1
                continue
            beg = idx
            while idx < n - m and arr[idx] == arr[idx + m]:
                idx += 1
            if idx - beg >= req:
                return True
        return False
