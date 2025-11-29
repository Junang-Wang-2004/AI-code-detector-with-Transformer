class Solution:
    def countSubarrays(self, nums, k):
        ans = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] & k != k:
                i += 1
                continue
            states = {}
            j = i
            while j < n:
                x = nums[j]
                if x & k != k:
                    break
                new_states = {}
                new_states[x] = new_states.get(x, 0) + 1
                for prev, cnt in states.items():
                    combined = prev & x
                    new_states[combined] = new_states.get(combined, 0) + cnt
                ans += new_states.get(k, 0)
                states = new_states
                j += 1
            i = j
        return ans
