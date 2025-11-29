class Solution:
    def getMaxLen(self, nums):
        maximum = 0
        idx = 0
        total = len(nums)
        while idx < total:
            if nums[idx] == 0:
                idx += 1
                continue
            seg_end = idx
            while seg_end < total and nums[seg_end] != 0:
                seg_end += 1
            seg_end -= 1
            negative_count = 0
            earliest_negative = -1
            for pos in range(idx, seg_end + 1):
                if nums[pos] < 0:
                    negative_count += 1
                    if earliest_negative == -1:
                        earliest_negative = pos
            segment_length = seg_end - idx + 1
            if negative_count % 2 == 0:
                maximum = max(maximum, segment_length)
            elif earliest_negative != -1:
                maximum = max(maximum, seg_end - earliest_negative)
            idx = seg_end + 1
        return maximum
