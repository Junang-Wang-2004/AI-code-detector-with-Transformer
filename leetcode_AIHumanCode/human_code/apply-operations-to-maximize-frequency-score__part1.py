# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, sliding window
class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        """
        nums.sort()
        result = left = curr = 0
        for right in range(len(nums)):
            # "-+  " => "-0+ "
            # "-0+ " => "--++"
            curr += nums[right]-nums[(left+right)//2]
            if not curr <= k:
                # "--++" => " -0+"
                # " -0+" => "  -+"
                curr -= nums[((left+1)+right)//2]-nums[left]
                left += 1
        return right-left+1


