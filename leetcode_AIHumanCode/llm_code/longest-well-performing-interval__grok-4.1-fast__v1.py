class Solution(object):
    def longestWPI(self, hours):
        n = len(hours)
        SHIFT = n
        SENTINEL = n + 1
        first_occurrence = [SENTINEL] * (2 * n + 1)
        first_occurrence[SHIFT] = -1
        maximum_length = 0
        current_balance = 0
        for position, work_hours in enumerate(hours):
            if work_hours > 8:
                current_balance += 1
            else:
                current_balance -= 1
            if current_balance > 0:
                maximum_length = max(maximum_length, position + 1)
            previous_balance = current_balance - 1
            previous_shifted = SHIFT + previous_balance
            if 0 <= previous_shifted < len(first_occurrence) and first_occurrence[previous_shifted] < SENTINEL:
                maximum_length = max(maximum_length, position - first_occurrence[previous_shifted])
            current_shifted = SHIFT + current_balance
            if first_occurrence[current_shifted] == SENTINEL:
                first_occurrence[current_shifted] = position
        return maximum_length
