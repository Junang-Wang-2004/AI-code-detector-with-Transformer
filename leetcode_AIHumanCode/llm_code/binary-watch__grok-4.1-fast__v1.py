class Solution:
    def readBinaryWatch(self, target):
        def count_set_bits(value):
            total = 0
            while value:
                total += value & 1
                value >>= 1
            return total

        valid_times = []
        for current_hour in range(12):
            for current_minute in range(60):
                if count_set_bits(current_hour) + count_set_bits(current_minute) == target:
                    valid_times.append(f"{current_hour}:{current_minute:02d}")
        return valid_times
