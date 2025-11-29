class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)
        for start in range(n):
            if nums[start] == 0:
                continue
            direction = nums[start]
            tortoise = start
            hare = start
            while True:
                t_next = (tortoise + nums[tortoise]) % n
                if nums[t_next] * direction <= 0:
                    break
                h_next1 = (hare + nums[hare]) % n
                if nums[h_next1] * direction <= 0:
                    break
                h_next2 = (h_next1 + nums[h_next1]) % n
                if nums[h_next2] * direction <= 0:
                    break
                tortoise = t_next
                hare = h_next2
                if tortoise == hare:
                    cycle_next = (tortoise + nums[tortoise]) % n
                    if cycle_next != tortoise:
                        return True
                    break
            current = start
            while nums[current] * direction > 0:
                next_pos = (current + nums[current]) % n
                nums[current] = 0
                current = next_pos
        return False
