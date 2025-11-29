class Solution:
    def divisibleTripletCount(self, nums, d):
        store = {}
        total = 0
        length = len(nums)
        for pos in range(length):
            cur_rem = nums[pos] % d
            total += store.get(cur_rem, 0)
            for earlier in range(pos):
                sum_mod = (nums[pos] + nums[earlier]) % d
                req_rem = (-sum_mod) % d
                store[req_rem] = store.get(req_rem, 0) + 1
        return total
