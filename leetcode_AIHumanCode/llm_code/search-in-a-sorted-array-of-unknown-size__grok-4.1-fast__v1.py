class Solution:
    def search(self, reader, target):
        lo, hi = 0, 19999
        while lo <= hi:
            mid = (lo + hi) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
