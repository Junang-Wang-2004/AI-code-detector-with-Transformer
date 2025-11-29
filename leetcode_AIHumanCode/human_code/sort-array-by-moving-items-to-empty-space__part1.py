# Time:  O(n)
# Space: O(n)

# greedy, sort
class Solution(object):
    def sortArray(self, nums):
        """
        """
        def min_moves(d):
            def index(x):
                return d*(len(nums)-1) if x == 0 else x-d

            lookup = [False]*len(nums)
            result = len(nums)
            for i in range(len(nums)):
                if lookup[nums[i]]:
                    continue
                l = 0
                while not lookup[nums[i]]:
                    lookup[nums[i]] = True
                    l += 1
                    i = index(nums[i])
                result -= 1
                if l >= 2:
                    result += 2
            return result-2*int(nums[d*(len(nums)-1)] != 0)

        return min(min_moves(0), min_moves(1))


