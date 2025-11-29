from collections import deque

class Solution:
    def findLexSmallestString(self, s, a, b):
        visited = {s}
        queue = deque([s])
        minimum = s
        n = len(s)
        while queue:
            current = queue.popleft()
            if current < minimum:
                minimum = current
            # Apply increment to odd-indexed positions
            incremented = list(current)
            for idx in range(1, n, 2):
                val = int(incremented[idx])
                incremented[idx] = str((val + a) % 10)
            inc_str = ''.join(incremented)
            if inc_str not in visited:
                visited.add(inc_str)
                queue.append(inc_str)
            # Apply left rotation by b positions
            rot_str = current[b:] + current[:b]
            if rot_str not in visited:
                visited.add(rot_str)
                queue.append(rot_str)
        return minimum
