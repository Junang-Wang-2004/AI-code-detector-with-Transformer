from collections import deque

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        possessed = set(initialBoxes)
        visited = set()
        ready = deque(b for b in initialBoxes if status[b])
        score = 0
        while ready:
            box = ready.popleft()
            if box in visited:
                continue
            visited.add(box)
            score += candies[box]
            for k in keys[box]:
                status[k] = 1
                if k in possessed and k not in visited:
                    ready.append(k)
            for b in containedBoxes[box]:
                possessed.add(b)
                if status[b] and b not in visited:
                    ready.append(b)
        return score
