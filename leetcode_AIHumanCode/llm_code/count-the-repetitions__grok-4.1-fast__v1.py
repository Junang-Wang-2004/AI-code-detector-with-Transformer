class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        len2 = len(s2)
        next_pos = [0] * len2
        gains = [0] * len2
        for start in range(len2):
            pos = start
            gain = 0
            for c in s1:
                if c == s2[pos]:
                    pos = (pos + 1) % len2
                    if pos == 0:
                        gain += 1
            next_pos[start] = pos
            gains[start] = gain

        pos = 0
        total = 0
        visited = {}
        steps = 0
        while steps < n1:
            if pos in visited:
                prev_steps, prev_total = visited[pos]
                cyc_steps = steps - prev_steps
                cyc_gain = total - prev_total
                num_cyc = (n1 - prev_steps) // cyc_steps
                total = prev_total + num_cyc * cyc_gain
                rem_steps = (n1 - prev_steps) % cyc_steps
                for _ in range(rem_steps):
                    total += gains[pos]
                    pos = next_pos[pos]
                return total // n2
            visited[pos] = (steps, total)
            total += gains[pos]
            pos = next_pos[pos]
            steps += 1
        return total // n2
