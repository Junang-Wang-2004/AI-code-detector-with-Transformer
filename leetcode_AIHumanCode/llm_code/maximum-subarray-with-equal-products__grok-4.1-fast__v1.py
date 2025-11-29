class Solution:
    def maxLength(self, arr):
        factor_list = [[] for _ in range(11)]
        for val in range(2, 11):
            if not factor_list[val]:
                for mult in range(val, 11, val):
                    factor_list[mult].append(val)
        max_window = 0
        prime_last = {}
        window_start = 0
        for window_end in range(len(arr)):
            current = arr[window_end]
            for pf in factor_list[current]:
                window_start = max(window_start, prime_last.get(pf, 0))
                prime_last[pf] = window_end + 1
            max_window = max(max_window, window_end - window_start + 1)
        return max_window
