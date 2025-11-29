from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums):
        seq1 = [nums[0]]
        seq2 = [nums[1]]
        sorted1 = SortedList()
        sorted1.add(nums[0])
        sorted2 = SortedList()
        sorted2.add(nums[1])
        for x in nums[2:]:
            gt1 = len(sorted1) - sorted1.bisect_right(x)
            gt2 = len(sorted2) - sorted2.bisect_right(x)
            if gt1 > gt2 or (gt1 == gt2 and len(seq1) <= len(seq2)):
                sorted1.add(x)
                seq1.append(x)
            else:
                sorted2.add(x)
                seq2.append(x)
        return seq1 + seq2
