class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        if not obstacles:
            return []
        unique = sorted(set(obstacles))
        mapping = {val: idx + 1 for idx, val in enumerate(unique)}
        size = len(unique)
        fenwick = [0] * (size + 2)
        answer = []
        for height in obstacles:
            pos = mapping[height]
            max_len = self.prefix_max(fenwick, pos)
            new_len = max_len + 1
            answer.append(new_len)
            self.modify(fenwick, pos, new_len, size)
        return answer

    def prefix_max(self, fenwick, pos):
        current_max = 0
        while pos > 0:
            current_max = max(current_max, fenwick[pos])
            pos -= pos & -pos
        return current_max

    def modify(self, fenwick, pos, value, max_size):
        while pos <= max_size:
            fenwick[pos] = max(fenwick[pos], value)
            pos += pos & -pos
