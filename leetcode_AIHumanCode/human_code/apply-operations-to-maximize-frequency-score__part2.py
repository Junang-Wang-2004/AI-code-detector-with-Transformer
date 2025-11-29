# Time:  O(nlogn)
# Space: O(1)
# sort, two pointers, sliding window
class Solution2(object):
    def maxFrequencyScore(self, nums, k):
        """
        """
        nums.sort()
        result = left = curr = 0
        for right in range(len(nums)):
            # "-+  " => "-0+ "
            # "-0+ " => "--++"
            curr += nums[right]-nums[(left+right)//2]
            while not curr <= k:
                # "--++" => " -0+"
                # " -0+" => "  -+"
                curr -= nums[((left+1)+right)//2]-nums[left]
                left += 1
            result = max(result, right-left+1)
        return result


