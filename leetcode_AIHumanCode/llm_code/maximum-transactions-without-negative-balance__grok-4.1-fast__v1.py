class Solution(object):
    def maxTransactions(self, transactions):
        nums = sorted(transactions, reverse=True)
        total = 0
        result = 0
        for val in nums:
            total += val
            if total >= 0:
                result += 1
            else:
                break
        return result
