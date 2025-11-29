# Time:  O(nlogn)
# Space: O(n)
# greedy
class Solution2(object):
    def minimalKSum(self, nums, k):
        """
        """
        result = prev = 0
        nums.append(float("inf"))
        for x in sorted(set(nums)):
            if not k:
                break
            cnt = min((x-1)-prev, k)
            k -= cnt
            result += ((prev+1)+(prev+cnt))*cnt//2
            prev = x
        return result
