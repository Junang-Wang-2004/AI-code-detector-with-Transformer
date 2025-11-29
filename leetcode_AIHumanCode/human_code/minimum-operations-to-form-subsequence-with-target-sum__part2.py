# Time:  O(nlogn)
# Space: O(1)
# codeforces, https://codeforces.com/problemset/problem/1303/D
# sort, greedy
class Solution2(object):
    def minOperations(self, nums, target):
        """
        """
        total = sum(nums)
        if total < target:
            return -1

        nums.sort()
        result = 0
        while target:
            x = nums.pop()
            if x <= target:
                target -= x
                total -= x
            elif total-x >= target:
                total -= x
            else:
                nums.append(x//2)
                nums.append(x//2)
                result += 1
        return result


