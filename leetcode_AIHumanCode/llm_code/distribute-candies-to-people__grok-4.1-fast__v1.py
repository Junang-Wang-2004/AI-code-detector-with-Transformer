class Solution:
    def distributeCandies(self, candies, num_people):
        low, high = 0, 200000
        while low < high:
            mid = low + (high - low + 1) // 2
            if mid * (mid + 1) // 2 <= candies:
                low = mid
            else:
                high = mid - 1
        full_steps = low
        extra = candies - full_steps * (full_steps + 1) // 2
        distribution = [0] * num_people
        cycles = full_steps // num_people
        extra_people = full_steps % num_people
        for person in range(num_people):
            times = cycles + (1 if person < extra_people else 0)
            distribution[person] = times * (person + 1) + num_people * (times * (times - 1) // 2)
        if extra > 0:
            next_person = full_steps % num_people
            distribution[next_person] += extra
        return distribution
