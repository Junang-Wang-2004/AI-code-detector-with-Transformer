class Solution:
    def longestMountain(self, arr):
        ans = 0
        n = len(arr)
        pos = 0
        while pos < n:
            up_beg = pos
            while pos < n - 1 and arr[pos + 1] > arr[pos]:
                pos += 1
            up_fin = pos
            dwn_beg = pos
            while pos < n - 1 and arr[pos + 1] < arr[pos]:
                pos += 1
            dwn_fin = pos
            if up_fin > up_beg and dwn_fin > up_fin:
                ans = max(ans, dwn_fin - up_beg + 1)
            if up_fin == up_beg and dwn_fin == up_beg:
                pos += 1
        return ans
