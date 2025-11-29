class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        position_map = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        frog_counts = [0] * 5
        max_needed = 0
        for ch in croakOfFrogs:
            if ch not in position_map:
                return -1
            pos = position_map[ch]
            if frog_counts[pos] == 0:
                if pos != 0:
                    return -1
                max_needed += 1
            else:
                frog_counts[pos] -= 1
            nxt = (pos + 1) % 5
            frog_counts[nxt] += 1
        for stage in range(1, 5):
            if frog_counts[stage] > 0:
                return -1
        return max_needed
