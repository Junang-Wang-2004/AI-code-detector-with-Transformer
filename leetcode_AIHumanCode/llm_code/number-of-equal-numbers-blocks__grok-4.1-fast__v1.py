# Definition for BigArray.
class BigArray:
    def at(self, index):
        pass
    def size(self):
        pass


class Solution:
    def countBlocks(self, nums):
        count = 0
        current = 0
        array_size = nums.size()
        while current < array_size:
            value = nums.at(current)
            lo = current
            hi = array_size - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums.at(mid) == value:
                    lo = mid + 1
                else:
                    hi = mid - 1
            block_end = hi
            current = block_end + 1
            count += 1
        return count
