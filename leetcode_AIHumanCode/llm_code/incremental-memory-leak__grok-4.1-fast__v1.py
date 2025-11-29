class Solution(object):
    def memLeak(self, memory1, memory2):
        def arith_sum(start, step, count):
            return count * (2 * start + (count - 1) * step) // 2

        def find_max_count(start, step, limit):
            if limit < 0:
                return 0
            left, right = 0, 2 * 10**9 + 5
            while left < right:
                middle = (left + right + 1) // 2
                if arith_sum(start, step, middle) <= limit:
                    left = middle
                else:
                    right = middle - 1
            return left

        big, small = memory1, memory2
        was_flipped = big < small
        if was_flipped:
            big, small = small, big
        gap = big - small
        first_phase = find_max_count(1, 1, gap)
        big -= arith_sum(1, 1, first_phase)
        if big == small:
            was_flipped = False
        second_phase_big = find_max_count(first_phase + 1, 2, big)
        second_phase_small = find_max_count(first_phase + 2, 2, small)
        big -= arith_sum(first_phase + 1, 2, second_phase_big)
        small -= arith_sum(first_phase + 2, 2, second_phase_small)
        if was_flipped:
            big, small = small, big
        moment = first_phase + second_phase_big + second_phase_small + 1
        return [moment, big, small]
