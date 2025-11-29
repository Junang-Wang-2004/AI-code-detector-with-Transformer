class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        def largest_possible_side(segments):
            if not segments:
                return 1
            sorted_unique = sorted(set(segments))
            if len(sorted_unique) == 0:
                return 1
            longest_run = 1
            active_run = 1
            for idx in range(1, len(sorted_unique)):
                if sorted_unique[idx] == sorted_unique[idx - 1] + 1:
                    active_run += 1
                else:
                    active_run = 1
                longest_run = max(longest_run, active_run)
            return longest_run + 1

        max_h = largest_possible_side(hBars)
        max_v = largest_possible_side(vBars)
        effective_side = min(max_h, max_v)
        return effective_side * effective_side
