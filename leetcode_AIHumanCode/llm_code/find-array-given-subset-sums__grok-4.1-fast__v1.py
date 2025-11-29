class Solution(object):
    def recoverArray(self, n, sums):
        current = sorted(sums)
        empty = 0
        outcome = []
        size = len(current)
        while size > 1:
            gap = current[0] - current[1]
            next_current = []
            ptr = 0
            includes_zero = False
            for idx in range(size):
                if ptr < len(next_current) and next_current[ptr] == current[idx]:
                    ptr += 1
                else:
                    moved = current[idx] - gap
                    if moved == empty:
                        includes_zero = True
                    next_current.append(moved)
            if includes_zero:
                outcome.append(gap)
            else:
                outcome.append(-gap)
                empty -= gap
            current = next_current
            size //= 2
        return outcome
