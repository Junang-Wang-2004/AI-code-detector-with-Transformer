class Solution:
    def maxBoxesInWarehouse(self, boxSizes, rackHeights):
        boxSizes.sort(key=lambda x: -x)
        lo, hi = 0, len(rackHeights) - 1
        count = 0
        for size in boxSizes:
            if lo > hi:
                break
            if size <= rackHeights[lo]:
                lo += 1
                count += 1
            elif size <= rackHeights[hi]:
                hi -= 1
                count += 1
        return count
