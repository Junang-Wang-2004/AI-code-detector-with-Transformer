class Solution(object):
    def makesquare(self, nums):
        perimeter = sum(nums)
        if perimeter % 4 != 0:
            return False
        edge = perimeter // 4
        if max(nums) > edge:
            return False
        nums.sort(reverse=True)
        piles = [0] * 4

        def assign(stick):
            if stick == len(nums):
                return True
            for slot in range(4):
                if piles[slot] + nums[stick] > edge:
                    continue
                piles[slot] += nums[stick]
                if assign(stick + 1):
                    return True
                piles[slot] -= nums[stick]
                if piles[slot] == 0:
                    break
            return False

        return assign(0)
