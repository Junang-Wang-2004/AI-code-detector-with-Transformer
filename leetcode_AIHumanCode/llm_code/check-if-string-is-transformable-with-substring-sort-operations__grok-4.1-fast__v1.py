class Solution:
    def isTransformable(self, s, t):
        positions = [[] for _ in range(10)]
        for idx, char in enumerate(s):
            positions[int(char)].append(idx)
        next_avail = [0] * 10
        for char in t:
            dig = int(char)
            if next_avail[dig] >= len(positions[dig]):
                return False
            pos_here = positions[dig][next_avail[dig]]
            for smaller_dig in range(dig):
                if next_avail[smaller_dig] < len(positions[smaller_dig]) and positions[smaller_dig][next_avail[smaller_dig]] < pos_here:
                    return False
            next_avail[dig] += 1
        return True
