from sortedcontainers import SortedList

class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        ans = []
        sorted_neg = SortedList()
        length = len(nums)
        for pos in range(length):
            if pos >= k:
                outgoing = nums[pos - k]
                if outgoing <= 0:
                    sorted_neg.remove(outgoing)
            incoming = nums[pos]
            if incoming <= 0:
                sorted_neg.add(incoming)
            if pos >= k - 1:
                if len(sorted_neg) >= x:
                    ans.append(sorted_neg[x - 1])
                else:
                    ans.append(0)
        return ans
