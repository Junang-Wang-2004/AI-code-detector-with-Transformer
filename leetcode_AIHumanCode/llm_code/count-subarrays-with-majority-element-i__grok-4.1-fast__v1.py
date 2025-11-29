class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n
        sz = 2 * n + 1
        fr = [0] * sz
        ps = [0] * sz
        z = offset
        fr[z] = 1
        ps[z] = 1
        bal = 0
        ans = 0
        for val in nums:
            bal += 1 if val == target else -1
            i = bal + offset
            fr[i] += 1
            ps[i] = ps[i - 1] + fr[i]
            ans += ps[i - 1]
        return ans
