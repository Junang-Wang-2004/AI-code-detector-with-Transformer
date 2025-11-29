# Time:  O(logn)
# Space: O(logn)

class Solution(object):
    def findKthNumber(self, n, k):
        """
        """
        result = 0

        cnts = [0] * 10
        for i in range(1, 10):
            cnts[i] = cnts[i - 1] * 10 + 1

        nums = []
        i = n
        while i:
            nums.append(i % 10)
            i /= 10

        total, target = n, 0
        i = len(nums) - 1
        while i >= 0 and k > 0:
            target = target*10 + nums[i]
            start = int(i == len(nums)-1)
            for j in range(start, 10):
                candidate = result*10 + j
                if candidate < target:
                    num = cnts[i+1]
                elif candidate > target:
                    num = cnts[i]
                else:
                    num = total - cnts[i + 1]*(j-start) - cnts[i]*(9-j)
                if k > num:
                    k -= num
                else:
                    result = candidate
                    k -= 1
                    total = num-1
                    break
            i -= 1

        return result


